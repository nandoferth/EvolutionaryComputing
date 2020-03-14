
"""
Vizcaino Lopez Fernando
13/03/2020
"""

import math
import random
import functools

class generateChromosome:

    population = []
    #SaveChromosome = []

    def __init__(self, L_chromosome, N_chromosomes):
        self.L_chromosome = L_chromosome
        self.N_chromosomes = N_chromosomes

    def GeneratePopulation(self):#GeneratePopulation->RandomChromosome
        for i in range(self.N_chromosomes):
            self.population.append(self.RandomChromosome())
    
    def RandomChromosome(self):
        chromosome = []
        for i in range(0,self.L_chromosome):
            if random.random()<0.1:
                chromosome.append(0)
            else:
                chromosome.append(1)
        return chromosome

    def DecodeChromosome(self):
        value = 0
        DecodePopulation=[]
        for j in range(self.N_chromosomes):
            for i in range(self.L_chromosome):
                value += 2**i*self.population[j][self.L_chromosome-(i+1)]
            DecodePopulation.append(value)
        return DecodePopulation
    """
    def SelectionChromosome(self, Chromosome):
        for i in range(self.N_chromosomes):
            self.SaveChromosome.append(self.population[i])
    """
    