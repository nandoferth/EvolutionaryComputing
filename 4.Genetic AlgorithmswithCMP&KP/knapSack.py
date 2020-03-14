def knapSack(W , wt , val , n): 
    if n == 0 or W == 0 : 
        return 0
    if (wt[n-1] > W): 
        return knapSack(W , wt , val , n-1) 
    else: 
        return max(val[n-1] + knapSack(W-wt[n-1] , wt , val , n-1), 
            knapSack(W , wt , val , n-1)) 
val = [5,11,18,26,35,30] 
wt = [1,2,3,4,5,6] 
W = 13
n = len(val) 
print (knapSack(W , wt , val , n))

val = [11,35,30] 
wt = [2,5,6] 
W = 13
n = len(val) 
print (knapSack(W , wt , val , n))

val = [5,11,26,35] 
wt = [1,2,4,5] 
W = 13
n = len(val) 
print (knapSack(W , wt , val , n))

val = [5,18,26,35] 
wt = [1,3,4,5] 
W = 13
n = len(val) 
print (knapSack(W , wt , val , n))