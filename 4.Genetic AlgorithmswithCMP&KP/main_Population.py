
"""
Vizcaino Lopez Fernando
13/03/2020
"""
import functools

from class_Population import generateChromosome

if __name__ == "__main__":
    chromosome = generateChromosome(16,10,16,13)
    chromosome.GeneratePopulation()
    chromosome.population.sort(key=functools.cmp_to_key(chromosome.CompareChromosomes))
    chromosome.EvaluateChromosomes()
    print("BEST")
    print("w:",chromosome.DecodepChromosome(0,0,chromosome.div_chromosome, chromosome.population[0],0),
        "v:",chromosome.DecodepChromosome(0,0,chromosome.div_chromosome, chromosome.population[0],1)
        )
    print(chromosome.FitnessPopulation)
    #chromosome.DecodepChromosome(0,chromosome.L_chromosome//2,chromosome.L_chromosome//2+chromosome.div_chromosome,chromosome.population[0],1)