
"""
Vizcaino Lopez Fernando
13/03/2020
"""

import math
import random
import functools
from knapSack import knapSack

class generateChromosome:

    population = []
    FitnessPopulation = []
    #SaveChromosome = []
    val = [5,11,18,26,35,30] 
    wt = [1,2,3,4,5,6] 

    def __init__(self, L_chromosome, N_chromosomes,div_chromosome,Weight):
        self.L_chromosome = L_chromosome
        self.N_chromosomes = N_chromosomes
        self.div_chromosome = div_chromosome//4
        self.Weight = Weight

    def GeneratePopulation(self):#GeneratePopulation->RandomChromosome
        for i in range(self.N_chromosomes):
            self.population.append(self.RandomChromosome())
            self.FitnessPopulation.append(0)
    
    def RandomChromosome(self):
        chromosome = []
        for i in range(0,self.L_chromosome):
            if random.random()<0.1:
                chromosome.append(0)
            else:
                chromosome.append(1)
        return chromosome

    def EvaluateChromosomes(self):
        for p in range(self.N_chromosomes):
            wtChromosome = self.DecodepChromosome(0,0,self.div_chromosome, self.population[p],0)
            valChromosome = self.DecodepChromosome(0,0,self.div_chromosome, self.population[p],1)
            #valChromosome = self.DecodepChromosome(0,self.L_chromosome//2,self.L_chromosome//2+self.div_chromosome,self.population[p],1)
            self.FitnessPopulation[p]=knapSack(self.Weight,self.wt,self.val,len(self.val))-knapSack(self.Weight,wtChromosome,valChromosome,len(valChromosome))
    
    def CompareChromosomes(self, chromosome1,chromosome2):
        wtChromosome1 = self.DecodepChromosome(0,0,self.div_chromosome,chromosome1,0)
        valChromosome1 = self.DecodepChromosome(0,0,self.div_chromosome,chromosome1,1)
        #valChromosome1 = self.DecodepChromosome(0,self.L_chromosome//2,self.L_chromosome//2+self.div_chromosome,chromosome1,1)
        wtChromosome2 = self.DecodepChromosome(0,0,self.div_chromosome,chromosome2,0)
        valChromosome2 = self.DecodepChromosome(0,0,self.div_chromosome,chromosome2,1)
        #valChromosome2 = self.DecodepChromosome(0,self.L_chromosome//2,self.L_chromosome//2+self.div_chromosome,chromosome2,1)
        KPf1 = knapSack(self.Weight,self.wt,self.val,len(self.val))-knapSack(self.Weight,wtChromosome1,valChromosome1,len(valChromosome1))
        KPf2 = knapSack(self.Weight,self.wt,self.val,len(self.val))-knapSack(self.Weight,wtChromosome2,valChromosome2,len(valChromosome2))
        if KPf1 < 0:
            return 1
        elif KPf2 < 0: #kSChromosome1<kSChromosome2
            return -1
        elif KPf1 == KPf2:
            return 0
        elif KPf1 > KPf2:
            return 1
        else:
            return -1

    def DecodepChromosome(self,endRec,start,endr,chromosome,wv):
        divChromosomeDecode = []
        while endRec < self.div_chromosome:
            value = 0
            for i in range(start,endr):
                value += 2**(i-start)*chromosome[endr-((i-start)+1)]
            endRec+=1
            start+=self.div_chromosome
            endr+=self.div_chromosome
            value = int(value*((len(self.val)-1)/(self.L_chromosome-1)))
            if wv==0:
                divChromosomeDecode.append(self.wt[value])
            else:
                divChromosomeDecode.append(self.val[value])
        return divChromosomeDecode
    