from ga.individual_int_vector import IntVectorIndividual
from warehouse.cell import Cell


class WarehouseIndividual(IntVectorIndividual):

    def __init__(self, problem: "WarehouseProblemGA", num_genes: int):
        super().__init__(problem, num_genes)
        # TODO
        self.problem = problem
        self.products = self.problem.products
        self.pairs = self.problem.pairs
        self.exit = self.problem.exit
        self.fitness = 0
        self.collisions = 0
        self.crossings = 0

    def compute_fitness(self) -> float:
        # TODO
        self.fitness = 0
        j = 0
        cell1 = self.forklifts[j]

        for i in range(len(self.genome)):
            if self.genome[i] <= len(self.products):
                self.fitness += self.get_pair_value(cell1, self.products[self.genome[i] - 1])
                cell1 = self.products[self.genome[i] - 1]
            else:
                self.fitness += self.get_pair_value(cell1, self.exit)
                j += 1
                cell1 = self.forklifts[j]

        self.fitness += self.get_pair_value(cell1, self.exit)

        # Penalizações por colisão e cruzamento

        all_path, steps = self.obtain_all_path()

        self.collisions = 0
        self.crossings = 0
        for i in range(steps):
            for j in range(len(all_path)):
                if i < len(all_path[j]):
                    for k in range(j+1, len(all_path)):
                        if j != k and i < len(all_path[k]):
                            if all_path[j][i] == all_path[k][i]:
                                self.fitness += 1
                                self.collisions += 1
                            if all_path[j][i] == all_path[k][i-1] and all_path[j][i-1] == all_path[k][i]:
                                self.fitness += 1
                                self.crossings += 1

        return self.fitness

    def obtain_all_path(self):
        # TODO
        all_path = []
        forklift_path = []
        j = 0
        steps = 0
        cell1 = self.forklifts[j]

        for i in range(len(self.genome)):
            if self.genome[i] <= len(self.products):
                forklift_path += self.get_agent_cells(cell1, self.products[self.genome[i] - 1])
                cell1 = self.products[self.genome[i] - 1]
            else:
                forklift_path += self.get_agent_cells(cell1, self.exit)
                j += 1
                cell1 = self.forklifts[j]

                forklift_path = self.remove_consecutive_duplicates(forklift_path)
                all_path.append(forklift_path)

                steps = len(forklift_path) if len(forklift_path) > steps else steps
                forklift_path = []

        forklift_path += self.get_agent_cells(cell1, self.exit)
        forklift_path = self.remove_consecutive_duplicates(forklift_path)

        all_path.append(forklift_path)
        steps = len(forklift_path) if len(forklift_path) > steps else steps

        return all_path, steps

    def __str__(self):
        string = 'Fitness: ' + f'{self.fitness}' + '\n'
        string += str (self.genome) + "\n\n"

        # TODO
        # Mostrar os produtos que cada forklift apanha

        j = 0
        string += "Forklift " + str(j+1) + ":\n["

        for i in range(len(self.genome)):
            if self.genome[i] <= len(self.products):
                string += " " + str(self.genome[i]) + " "
            else:
                string += "]"
                j += 1
                string += "\n\nForklift " + str(j + 1) + ":\n["

        string += "]"

        string += "\n\nCollisions: " + str(self.collisions)
        string += "\nCrossings: " + str(self.crossings)

        return string

    def better_than(self, other: "WarehouseIndividual") -> bool:
        return True if self.fitness < other.fitness else False

    # __deepcopy__ is implemented here so that all individuals share the same problem instance
    def __deepcopy__(self, memo):
        new_instance = self.__class__(self.problem, self.num_genes)
        new_instance.genome = self.genome.copy()
        new_instance.fitness = self.fitness
        new_instance.pairs = self.pairs.copy()
        new_instance.products = self.products.copy()
        new_instance.forklifts = self.forklifts.copy()
        new_instance.exit = self.exit
        new_instance.problem = self.problem
        new_instance.num_genes = self.num_genes
        new_instance.collisions = self.collisions
        new_instance.crossings = self.crossings
        # TODO
        return new_instance

    def get_pair_value(self, cell1: Cell, cell2: Cell) -> int:
        for pair in self.pairs:
            if pair.cell1 == cell1 and pair.cell2 == cell2 or pair.cell1 == cell2 and pair.cell2 == cell1:
                return pair.value
        return 0

    def get_agent_cells(self, cell1: Cell, cell2: Cell):
        for pair in self.pairs:
            if pair.cell1 == cell1 and pair.cell2 == cell2:
                return pair.path_cells
            elif pair.cell1 == cell2 and pair.cell2 == cell1:
                reversed_array = pair.path_cells[::-1]
                return reversed_array
        return None

    @staticmethod
    def remove_consecutive_duplicates(forklift_path) -> []:
        new_path = []
        previous_cell = None

        for cell in forklift_path:
            if cell != previous_cell:
                new_path.append(cell)
                previous_cell = cell

        return new_path

    # Para obter o genome e os produtos no gui.py
    def obtain_genome_and_products(self):
        return self.genome, self.products
