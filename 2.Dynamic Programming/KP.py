
def knapSack(c, wt, val, n): 
    K = [[0 for x in range(c+1)] for x in range(n+1)] 
  
    # Build table K[][] in bottom up manner 
    for x in range(n+1): 
        for w in range(c+1): 
            if x==0 or w==0: 
                K[x][w] = 0
            elif wt[x-1] <= w: 
                K[x][w] = max(val[x-1] + K[x-1][w-wt[x-1]],  K[x-1][w]) 
            else: 
                K[x][w] = K[x-1][w] 
        #print(wt[x],val[x],K[x])
    return K

def main ():
    w = [5,10,15,20,25,30] 
    v = [3,9,6,12,15,18] 
    c = 30
    n = len(v) 
    K = knapSack(c, w, v, n)
    print("w v  0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29")
    for i in range(7):
        if i==0:
            print("0 0",K[i])
        else :
            print(w[i-1],v[i-1],K[i])
    #print(K)
    mvx=n-1
    wt = int(input("Choose a weigh between 1-11: "))
    while K[n][wt] != 0 :
        if K[n][wt] == K[n-1][wt]:
            n-=1
            mvx-=1
        else: 
            wt-=v[mvx]
            print("w:",w[mvx],"v:",v[mvx])
main()