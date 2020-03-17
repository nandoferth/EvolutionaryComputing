
"""
Vizcaino Lopez Fernando
13/03/2020
15/03/2020
"""
import functools
from knapSack import *
from class_Population import generateChromosome
from Coin_Change import CoinChange

if __name__ == "__main__":
    while 1:
        option = int(input("1.knapSack\n2.Coin Change\n"))
        if option == 1:
            chromosome = generateChromosome(16,30,16,13)
            chromosome.GeneratePopulation()
            chromosome.population.sort(key=functools.cmp_to_key(chromosome.CompareChromosomes))
            chromosome.EvaluateChromosomes()
            i=1
            wtot=knapSack(chromosome.Weight,chromosome.wt,chromosome.val,len(chromosome.val))
            while chromosome.wttot<=wtot:
                if chromosome.wttot==wtot:
                    break
                else:
                    print("Generation #",i)
                    chromosome.nextGeneration()
                i+=1
            chromosome.population[:]=[]
            chromosome.populationCopy[:]=[]
            chromosome.FitnessPopulation[:]=[]
            chromosome.wttot=0
            #chromosome.DecodepChromosome(0,chromosome.L_chromosome//2,chromosome.L_chromosome//2+chromosome.div_chromosome,chromosome.population[0],1)
        elif option == 2:
            chromosomeCoin = CoinChange(16,10,4,30)
            chromosomeCoin.GeneratePopulation()
            chromosomeCoin.population.sort(key=functools.cmp_to_key(chromosomeCoin.CompareChromosomes))
            chromosomeCoin.EvaluateChromosomes()
            i=1
            while 1:
                if chromosomeCoin.Coin==chromosomeCoin.cointot1:
                    break
                else:
                    print("Generation #",i)
                    chromosomeCoin.nextGeneration()
                i+=1
            chromosomeCoin.population[:]=[]
            chromosomeCoin.populationCopy[:]=[]
            chromosomeCoin.FitnessPopulation[:]=[]
            chromosomeCoin.Coin=0
        else:
            break

"""print("BEST")
            print("w:",chromosome.DecodepChromosome(0,0,chromosome.div_chromosome, chromosome.population[0],0),
                "v:",chromosome.DecodepChromosome(0,0,chromosome.div_chromosome, chromosome.population[0],1),
                "KP:", 
                )
            print(chromosome.FitnessPopulation)"""