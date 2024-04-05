import numpy as np

from ga.genetic_algorithm import GeneticAlgorithm
from ga.individual_int_vector import IntVectorIndividual
from ga.genetic_operators.mutation import Mutation

class Mutation2(Mutation):
    def __init__(self, probability):
        super().__init__(probability)

    def mutate(self, ind: IntVectorIndividual) -> None:
        # TODO
        # Inversion mutation

        # Copy the individual to avoid modifying the original
        mutated_individual = np.copy(ind.genome)

        # Select two random positions in the individual's genome
        pos1 = GeneticAlgorithm.rand.randint(0, len(mutated_individual) - 1)
        pos2 = GeneticAlgorithm.rand.randint(0, len(mutated_individual) - 1)

        # Ensure pos1 is smaller than pos2
        pos1, pos2 = min(pos1, pos2), max(pos1, pos2)

        # Reverse the sequence between pos1 and pos2
        while pos1 < pos2:
            mutated_individual[pos1], mutated_individual[pos2] = mutated_individual[pos2], mutated_individual[pos1]
            pos1 += 1
            pos2 -= 1

        ind.genome = mutated_individual.tolist()

    def __str__(self):
        return "Mutation 2 (" + f'{self.probability}' + ")"
