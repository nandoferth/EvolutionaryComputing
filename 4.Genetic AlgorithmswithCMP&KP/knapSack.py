
"""
Vizcaino Lopez Fernando
13/03/2020
15/03/2020
reference https://www.geeksforgeeks.org/python-program-for-dynamic-programming-set-10-0-1-knapsack-problem/
"""

def knapSack(W , wt , val , n): 
    if n == 0 or W == 0 : 
        return 0
    if (wt[n-1] > W): 
        return knapSack(W,wt,val,n-1) 
    else: 
        return max(val[n-1] + knapSack(W-wt[n-1] , wt , val , n-1), knapSack(W , wt , val , n-1))

def CC(coin,n):
    if n==-1:
        return 0
    if coin[n]==1:
        return 1
    else:
        return CC(coin,n-1)+coin[n]
"""coin=[0,1,2,5,10,20,50]
n = len(coin)-1
print(CC(coin,n))

val = [5,18,26,35] 
wt = [1,3,4,5] 
W = 13
n = len(val) 
print (knapSack(W , wt , val , n))"""