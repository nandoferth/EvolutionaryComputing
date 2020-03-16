
"""
Vizcaino Lopez Fernando
13/03/2020
15/03/2020
"""

import math
import random
import functools
from knapSack import knapSack

class generateChromosome:

    population = []
    populationCopy = []
    FitnessPopulation = []
    wttot=0
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

    def create_wheel(self):
        Lwheel=self.N_chromosomes*10
        maxv=max(self.FitnessPopulation)
        acc=0
        for p in range(self.N_chromosomes):
            acc+=maxv-self.FitnessPopulation[p]
        fraction=[]
        for p in range(self.N_chromosomes):
            fraction.append( float(maxv-self.FitnessPopulation[p])/acc)
            if fraction[-1]<=1.0/Lwheel:
                fraction[-1]=1.0/Lwheel
        fraction[0]-=(sum(fraction)-1.0)/2
        fraction[1]-=(sum(fraction)-1.0)/2
        wheel=[]
        pc=0
        for f in fraction:
            Np=int(f*Lwheel)
            for i in range(Np):
                wheel.append(pc)
            pc+=1
        return wheel

    def nextGeneration(self):
        self.populationCopy = self.population[:]
        crossover_point=self.L_chromosome//2
        prob_m=0.5
        self.population.sort(key=functools.cmp_to_key(self.CompareChromosomes))
        self.wttot=knapSack(self.Weight,self.DecodepChromosome(0,0,self.div_chromosome,self.population[0],0),self.DecodepChromosome(0,0,self.div_chromosome,self.population[0],1),4)
        print("Best solution so far:")
        print(
            "W:", str(self.DecodepChromosome(0,0,self.div_chromosome,self.population[0],0)), 
            "V:", str(self.DecodepChromosome(0,0,self.div_chromosome,self.population[0],1)),
            "Weight",self.wttot,
            "Weight_Total:", knapSack(self.Weight,self.wt,self.val,len(self.val)),
            #"Def:", min(self.FitnessPopulation)
        )
        self.populationCopy[0]=self.population[0]
        self.populationCopy[1]=self.population[1]
        for i in range(0,(self.N_chromosomes-2)//2):
            roulette=self.create_wheel()
            #Two parents are selected
            p1=random.choice(roulette)
            p2=random.choice(roulette)
            #Two descendants are generated
            o1=self.population[p1][0:crossover_point]
            o1.extend(self.population[p2][crossover_point:self.L_chromosome])
            o2=self.population[p2][0:crossover_point]
            o2.extend(self.population[p1][crossover_point:self.L_chromosome])
            #Each descendant is mutated with probability prob_m
            if random.random() < prob_m:
                o1[int(round(random.random()*(self.L_chromosome-1)))]^=1
            if random.random() < prob_m:
                o2[int(round(random.random()*(self.L_chromosome-1)))]^=1
            #The descendants are added to F1
            self.populationCopy[2+2*i]=o1
            self.populationCopy[3+2*i]=o2
        self.population[:]=self.populationCopy[:]
