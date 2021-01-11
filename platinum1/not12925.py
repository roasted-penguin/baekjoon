import math
def digits3(n):
    binary = list()
    while n>0:
        binary.append(n%2)
        n //= 2
    l = binary.length()
    arr = list()
    arr.append([3,1])
    a0, b0 = 3, 1
    for i in range(l-1):
        a1 = math.pow(a0,2) + 5*math.pow(b0,2)
        b1 = 2*a0*b0
    

T = int(input())
for i in range(T):
    N = int(input())
    print(digits3(N))
