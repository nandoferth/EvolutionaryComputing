
"""
Vizcaino Lopez Fernando
13/03/2020
15/03/2020
"""
import functools
from knapSack import knapSack

from class_Population import generateChromosome

if __name__ == "__main__":
    chromosome = generateChromosome(16,30,16,13)
    chromosome.GeneratePopulation()
    chromosome.population.sort(key=functools.cmp_to_key(chromosome.CompareChromosomes))
    chromosome.EvaluateChromosomes()
    """print("BEST")
    print("w:",chromosome.DecodepChromosome(0,0,chromosome.div_chromosome, chromosome.population[0],0),
        "v:",chromosome.DecodepChromosome(0,0,chromosome.div_chromosome, chromosome.population[0],1),
        "KP:", 
        )
    print(chromosome.FitnessPopulation)"""
    i=1
    wtot=knapSack(chromosome.Weight,chromosome.wt,chromosome.val,len(chromosome.val))
    while chromosome.wttot<=wtot:
        if chromosome.wttot==wtot:
            break
        else:
            print("Generation #",i)
            chromosome.nextGeneration()
        i+=1
    #chromosome.DecodepChromosome(0,chromosome.L_chromosome//2,chromosome.L_chromosome//2+chromosome.div_chromosome,chromosome.population[0],1)