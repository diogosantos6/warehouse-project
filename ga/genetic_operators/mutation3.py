import numpy as np

from ga.genetic_algorithm import GeneticAlgorithm
from ga.individual_int_vector import IntVectorIndividual
from ga.genetic_operators.mutation import Mutation

class Mutation3(Mutation):
    def __init__(self, probability):
        super().__init__(probability)

    def mutate(self, ind: IntVectorIndividual) -> None:
        # TODO
        # Displacement mutation
        # Copy the individual to avoid modifying the original
        mutated_individual = np.copy(ind.genome)

        # Select two random positions in the individual's genome
        pos1 = GeneticAlgorithm.rand.randint(0, len(mutated_individual) - 1)
        pos2 = GeneticAlgorithm.rand.randint(0, len(mutated_individual) - 1)

        print(pos1, pos2)

        # Ensure pos1 is smaller than pos2
        pos1, pos2 = min(pos1, pos2), max(pos1, pos2)

        # Extract the sequence between pos1 and pos2
        sequence = mutated_individual[pos1:pos2 + 1]

        # Remove the sequence from the individual's genome
        mutated_individual = np.delete(mutated_individual, np.arange(pos1, pos2 + 1))

        # Select a random position to insert the sequence
        insert_pos = GeneticAlgorithm.rand.randint(0, len(mutated_individual))

        # Insert the sequence at the chosen position
        mutated_individual = np.insert(mutated_individual, insert_pos, sequence)

        ind.genome = mutated_individual.tolist()

    def __str__(self):
        return "Mutation 3 (" + f'{self.probability}' + ")"
