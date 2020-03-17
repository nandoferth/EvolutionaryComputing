
import random
import functools
from knapSack import CC
class CoinChange:
    population = []
    populationCopy = []
    FitnessPopulation = []
    Cointot=0
    val = [0,1,2,5,10,20,50]
    cointot1=0

    def __init__(self, L_chromosome, N_chromosomes,div_chromosome,Coin):
        self.L_chromosome = L_chromosome
        self.N_chromosomes = N_chromosomes
        self.div_chromosome = div_chromosome
        self.Coin = Coin

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
            CoinChromosome = self.DecodepChromosome(0,0,self.div_chromosome, self.population[p])
            self.FitnessPopulation[p]=self.Coin-CC(CoinChromosome,len(CoinChromosome)-1)
        print("m",self.FitnessPopulation)
            
    def DecodepChromosome(self,endRec,start,endr,chromosome):
        divChromosomeDecode = []
        while endRec < self.div_chromosome:
            value = 0
            for i in range(start,endr):
                value += 2**(i-start)*chromosome[endr-((i-start)+1)]
            endRec+=1
            start+=self.div_chromosome
            endr+=self.div_chromosome
            value = int(value*((len(self.val)-1)/(self.L_chromosome-1)))
            divChromosomeDecode.append(self.val[value])
        return divChromosomeDecode

    def CompareChromosomes(self, chromosome1,chromosome2):
        CoinChromosome1 = self.DecodepChromosome(0,0,self.div_chromosome,chromosome1)
        CoinChromosome2 = self.DecodepChromosome(0,0,self.div_chromosome,chromosome2)
        Coinf1 = self.Coin-CC(CoinChromosome1,len(CoinChromosome1)-1)
        Coinf2 = self.Coin-CC(CoinChromosome2,len(CoinChromosome2)-1)
        if Coinf1 < 0:
            return 1
        elif Coinf2 < 0: #kSChromosome1<kSChromosome2
            return -1
        elif Coinf1 == Coinf2:
            return 0
        elif Coinf1 > Coinf2:
            return 1
        else:
            return -1

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
        ss=self.DecodepChromosome(0,0,self.div_chromosome,self.population[0])
        self.wttot=CC(ss,len(ss)-1)
        self.cointot1=CC(ss,len(ss)-1)
        print("Best solution so far:")
        print(
            "W:", str(self.DecodepChromosome(0,0,self.div_chromosome,self.population[0])),
            "Weight",self.cointot1,
            "Weight_Total:", self.Coin
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
        ss[:]=[]