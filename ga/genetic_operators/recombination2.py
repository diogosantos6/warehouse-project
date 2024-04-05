from ga.genetic_algorithm import GeneticAlgorithm
from ga.individual import Individual
from ga.genetic_operators.recombination import Recombination

class Recombination2(Recombination):

    def __init__(self, probability: float):
        super().__init__(probability)

    def recombine(self, ind1: Individual, ind2: Individual) -> None:
        # TODO
        # Order Crossover (OX)
        # Step 1: Select a random substring from parent 1
        substring_start = GeneticAlgorithm.rand.randint(0, len(ind1.genome) - 1)
        substring_end = GeneticAlgorithm.rand.randint(substring_start + 1, len(ind1.genome))
        substring = ind1.genome[substring_start:substring_end]

        # Step 2: Copying to child the substring from parent 1
        child1 = [-1] * len(ind1.genome)
        child1[substring_start:substring_end] = substring

        # Step 3: Create a sequence of genes needed by child1 from parent2
        genes_needed = [gene for gene in ind2.genome if gene not in substring]

        # Step 4: Place the genes needed into child1 (from left to right)
        genes_index = 0
        for i in range(len(ind1.genome)):
            if child1[i] == -1:
                child1[i] = genes_needed[genes_index]
                genes_index += 1

        # Step 5: Select substring from parent 2
        substring = ind2.genome[substring_start:substring_end]

        # Step 6: Copying to child 2 the substring from parent2
        child2 = [-1] * len(ind2.genome)
        child2[substring_start:substring_end] = substring

        # Step 7: Create a sequence of genes needed by child2 from parent1
        genes_needed = [gene for gene in ind1.genome if gene not in substring]

        # Step 8: Place the genes needed into child2 (from left to right)
        genes_index = 0
        for i in range(len(ind2.genome)):
            if child2[i] == -1:
                child2[i] = genes_needed[genes_index]
                genes_index += 1

        ind1.genome = child2
        ind2.genome = child1

    def __str__(self):
        return "Recombination 2 (" + f'{self.probability}' + ")"
