
from class_Population import generateChromosome

if __name__ == "__main__":
    chromosome = generateChromosome(15,10)
    chromosome.GeneratePopulation()
    print(chromosome.DecodeChromosome())