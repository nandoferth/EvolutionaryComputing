
def lv(a,b,x,y): 
    mz = [[0 for i in range(x)] for j in range(y)]

    print("ab",b[0],"", b[1],"", b[2],"", b[3],"", b[4],"", b[5],"", b[6],"", b[7],"", b[8],"", b[9])
    for i in range(y):
        for j in range(x):
            if i == 0:
                mz[i][j]=j
            elif j == 0:
                mz[i][j] = i
            elif a[i]==b[j]:
                mz[i][j]=mz[i-1][j-1]
            else:
                mz[i][j] = 1 + min(mz[i-1][j],mz[i][j-1],mz[i-1][j-1])
        print(a[i],mz[i])
    print(mz[i][j])
    mz = [[0 for i in range(y)] for j in range(x)]
    
    print("ab",a[0],"", a[1],"", a[2],"", a[3],"", a[4],"", a[5],"", a[6])
    for i in range(x):
        for j in range(y):
            if i == 0:
                mz[i][j]=j
            elif j == 0:
                mz[i][j] = i
            elif b[i]==a[j]:
                mz[i][j]=mz[i-1][j-1]
            else:
                mz[i][j] = 1 + min(mz[i-1][j],mz[i][j-1],mz[i-1][j-1])
        print(b[i],mz[i])
    print(mz[i][j])
    return mz

def main ():
    b = "/compnting"
    a = "/school"
    x = len(b)
    y = len(a)
    lv(a, b, x, y)
main()