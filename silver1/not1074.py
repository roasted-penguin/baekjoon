def makeZ(arr,level,n):
    if level == n:
        return arr
    else:
        powerr = pow(2,level+1)
        power = pow(4,level)
        ARR = [[0 for _ in range(powerr)] for _ in range(powerr)]
        for i in range(powerr):
            for j in range(powerr):
                pwr = powerr//2
                num = 0
                if i < pwr and j < pwr:
                    num = arr[i][j]
                elif i < pwr and j >= pwr:
                    num = power + arr[i][j-pwr]
                elif i >= pwr and j < pwr:
                    num = 2*power + arr[i-pwr][j]
                else:
                    num = 3*power + arr[i-pwr][j-pwr]
                    
                ARR[i][j] = num
        print(ARR)
        #ARR = [[z,z+power],[z+2*power,z+3*power]]
        return makeZ(ARR,level+1,n)

N, r, c = map(int,input().split())
z = [[0,1],[2,3]]

theZ = makeZ(z,1,N)
print(theZ[r][c])
