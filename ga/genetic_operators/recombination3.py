from ga.genetic_algorithm import GeneticAlgorithm
from ga.genetic_operators.recombination import Recombination
from ga.individual import Individual

class Recombination3(Recombination):

    def __init__(self, probability: float):
        super().__init__(probability)

    def recombine(self, ind1: Individual, ind2: Individual) -> None:
        # TODO
        # Position-Based Crossover (POS)
        positions = GeneticAlgorithm.rand.sample(range(len(ind1.genome)),
                                                 GeneticAlgorithm.rand.randint(1, len(ind1.genome)))

        # Sort positions
        for i in range(len(positions)):
            for j in range(len(positions)):
                if positions[i] < positions[j]:
                    positions[i], positions[j] = positions[j], positions[i]

        child1 = [-1] * len(ind1.genome)
        child2 = [-1] * len(ind1.genome)

        # Step 2: Copy genes from parent1 to child1 at selected positions and vice versa
        for position in positions:
            child1[position] = ind1.genome[position]
            child2[position] = ind2.genome[position]

        # Step 3: Get genes needed for child1 and child2
        genes_needed_child1 = [gene for gene in ind2.genome if gene not in child1]
        genes_needed_child2 = [gene for gene in ind1.genome if gene not in child2]

        ind1.genome = self.insert_genes(child2, genes_needed_child2)
        ind2.genome = self.insert_genes(child1, genes_needed_child1)

    def insert_genes(self, child, genes_needed):
        genes_index = 0
        for i in range(len(child)):
            if child[i] == -1:  # Find unfixed positions represented by -1
                child[i] = genes_needed[genes_index]  # Place the genes into unfixed positions
                genes_index += 1
        return child

    def __str__(self):
        return "Recombination 3 (" + f'{self.probability}' + ")"