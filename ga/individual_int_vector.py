
from abc import abstractmethod

import numpy as np

from ga.problem import Problem
from ga.individual import Individual


class IntVectorIndividual(Individual):

    def __init__(self, problem: Problem, num_genes: int):
        super().__init__(problem, num_genes)
        # TODO
        self.forklifts = self.problem.forklifts
        self.genome = np.random.permutation(num_genes + len(self.forklifts) - 1) + 1

        # fatorial do numero de genes
        # print("Número de combinações: ", np.math.factorial(len(self.genome)))

    def swap_genes(self, other, index: int):
        aux = self.genome[index]
        self.genome[index] = other.genome[index]
        other.genome[index] = aux

    @abstractmethod
    def compute_fitness(self) -> float:
        pass

    @abstractmethod
    def better_than(self, other: "IntVectorIndividual") -> bool:
        pass
