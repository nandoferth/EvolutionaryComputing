
import math
import random
import functools

L_chromosome=15
N_chromosomes=10
N_chains=2**(L_chromosome//3)
a=0
b=5
F0=[]
fitness_values=[]
crossover_point=L_chromosome//3
prob_m=0.5

def random_chromosome(L_chromosome):
    chromosome=[]*L_chromosome
    for i in range(0,L_chromosome):
        if random.random()<0.5:
            chromosome.append(0)
        else:
            chromosome.append(1)
    return chromosome


for i in range(0,N_chromosomes):
    F0.append(random_chromosome(L_chromosome))
    fitness_values.append(0)

def decode_chromosome(chromosome):
    L_chromosome,N_chains,a,b
    value=0
    #print(chromosome)
    for p in range(0,4):
        value += math.pow(2,p)*chromosome[(L_chromosome//3-(1+p))]
    #value = a+(b-a)*value//(N_chains-1)
    value = int(value/(31/b))
    return value
    #return a+(b-a)*(value)/(N_chains-1) #in Python3, conversion to float is not needed

def decode_chromosome2(chromosome):
    L_chromosome,N_chains,a,b
    value=0
    #print(chromosome)
    for p in range(5,9):
        value += math.pow(2,p-5)*chromosome[14-p]
    #value = a+(b-a)*value//(N_chains-1)
    value = int(value/(31/b))
    return value
def decode_chromosome3(chromosome):
    L_chromosome,N_chains,a,b
    value=0
    #print(chromosome)
    for p in range(10,14):
        value += math.pow(2,p-10)*chromosome[24-(p)]
    #value = a+(b-a)*value//(N_chains-1)
    value = int(value/(31/b))
    return value

def f(x,y,z,n):
    W = 6
    val = [6, 10, 12, 15, 20, 5] 
    wt = [1, 2, 3, 4, 5, 6] 
    if n == 0 or W == 0 : 
        return 0
    if (wt[n-1] > W):
        return f(W , wt , val , n-1) 
    else: 
        return max(val[n-1] + f(W-wt[n-1] , wt , val , n-1), f(W , wt , val , n-1)) 
        #return max(val[n-1] + knapSack(W-wt[n-1] , wt , val , n-1), knapSack(W , wt , val , n-1)) 

def evaluate_chromosomes():
    global F0

    for p in range(N_chromosomes):
        v=decode_chromosome(F0[p])
        m=decode_chromosome2(F0[p])
        n=decode_chromosome3(F0[p])
        #print("v:", v)
        fitness_values[p]=f(v,m,n,6)
        #print("f:", fitness_values[p])

def compare_chromosomes(chromosome1,chromosome2):
    n = 6
    vc1=decode_chromosome(chromosome1)
    vc11=decode_chromosome2(chromosome1)
    vc111=decode_chromosome3(chromosome1)
    vc2=decode_chromosome(chromosome2)
    vc22=decode_chromosome2(chromosome2)
    vc222=decode_chromosome3(chromosome2)
    #print(vc1,vc11,vc111,n)
    #print(vc2,vc22,vc222)
    fvc1=f(vc1,vc11,vc111,n)
    fvc2=f(vc2,vc22,vc222,n)
    if fvc1 > fvc2:
        print("1")
        return 1
    elif fvc1 == fvc2:
        print("0")
        return 0
    else: #fvg1<fvg2
        print("-1")
        return -1

Lwheel=N_chromosomes*10

def create_wheel():
    global F0,fitness_values

    maxv=max(fitness_values)
    acc=1
    for p in range(N_chromosomes):
        acc+=maxv-fitness_values[p]
    fraction=[]
    for p in range(N_chromosomes):
        fraction.append( (maxv-fitness_values[p])//acc)
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

F1=F0[:]

def nextgeneration():
    F0.sort(key=functools.cmp_to_key(compare_chromosomes))
    print( "Best solution so far:" )
    #print( "f(1."+str(decode_chromosome(F0[0]))+",2."+str(decode_chromosome2(F0[0]))+"3."+str(decode_chromosome3(F0[0]))+")= "+ 
    #str(f(decode_chromosome(F0[0]), decode_chromosome2(F0[0]),decode_chromosome3(F0[0]),6)) )
                                                                    
    #elitism, the two best chromosomes go directly to the next generation
    F1[0]=F0[0]
    F1[1]=F0[1]
    for i in range(0,(N_chromosomes-2)//2):
        roulette=create_wheel()
        #Two parents are selected
        p1=random.choice(roulette)
        p2=random.choice(roulette)
        #Two descendants are generated
        o1=F0[p1][0:crossover_point]
        o1.extend(F0[p2][crossover_point:L_chromosome])
        o2=F0[p2][0:crossover_point]
        o2.extend(F0[p1][crossover_point:L_chromosome])
        #Each descendant is mutated with probability prob_m
        if random.random() < prob_m:
            o1[int(round(random.random()*(L_chromosome-1)))]^=1
        if random.random() < prob_m:
            o2[int(round(random.random()*(L_chromosome-1)))]^=1
        #The descendants are added to F1
        F1[2+2*i]=o1
        F1[3+2*i]=o2

    #graph_f()
    #graph_population(F0,w,s,s,xo,yo,'red')
    #graph_population(F1,w,s,s*0.5,xo,yo,'green')
    #The new generation replaces the old one
    F0[:]=F1[:]

if __name__ == "__main__":
    #print(F0)
    print(F0.sort(key=functools.cmp_to_key(compare_chromosomes)))
    evaluate_chromosomes()
    #print(F0)
    while 1:
        nextgeneration()
        option = int(input("Continue? "))
        if option ==1:
            break
    