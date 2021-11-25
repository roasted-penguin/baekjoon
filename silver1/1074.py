
#크기 초과(배열크기 4^N)
"""
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
        #print(ARR)
        #ARR = [[z,z+power],[z+2*power,z+3*power]]
        return makeZ(ARR,level+1,n)

N, r, c = map(int,input().split())
z = [[0,1],[2,3]]

theZ = makeZ(z,1,N)
print(theZ[r][c])
"""

N, r, c = map(int,input().split())
R, C = 0, 0

power = 0
while r != 0:
    if r % 2 == 1:
        R += 2*pow(4,power)
    r //= 2
    power += 1

power = 0
while c != 0:
    if c % 2 == 1:
        C += pow(4,power)
    c //= 2
    power += 1

print(R+C)
