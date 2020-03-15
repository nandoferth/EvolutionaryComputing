
def cmp(t, d, tam):
    cmp = [[0,1,2,3,4,5,6,7,8,9]]

    for i in range(tam):
        cmp.append([0]*t)
    print("mc",cmp[0][0],"", cmp[0][1],"", cmp[0][2],"", cmp[0][3],"", cmp[0][4],"", cmp[0][5],"", cmp[0][6],"", cmp[0][7],"", cmp[0][8],"", cmp[0][9])
    for y in range(tam):
        #print(d[y])
        for x in range(t):
            if x >= d[y]:
                cmp[y+1][x] = min(cmp[y][x],cmp[y+1][x-d[y]]+1)
            else:
                cmp[y+1][x] = cmp[y][x]
        print(d[y],cmp[y+1])
    #print(cmp)
    return cmp

def main ():
    
    T  = 9
    d = [1, 2, 5]
    tam = len(d)
    mejor = cmp(T+1, d, tam)
    mvY=tam-1
    moneda = int(input("Choose a coin between 1-9: "))

    while moneda != 0 :
        if tam != 0:
            if mejor[tam][moneda] == mejor[tam-1][moneda]:
                tam-=1
                mvY-=1
        else: 
            tam+=1
            mvY+=1
        print(d[mvY])
        moneda-=d[mvY]

main()