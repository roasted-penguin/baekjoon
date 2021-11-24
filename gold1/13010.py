import math

def d(n,m):
    ans = 0
    for i in range(1,int(math.sqrt(n))+1):
        if n%i == 0:
            ans += 1
            if i*i < n:
                ans += 1
        if ans > m:
            break
    if ans == m:
        return True
    else:
        return False

n = int(input())
l = int(math.log2(n))
bool = True

while l>1:
    k = int(n**(1/l))
    if (k+1)**l == n:
        k = k+1
        if d(k,l):
            bool = False
            print(k)
            break
    elif (k-1)**l == n:
        k = k-1
        if d(k,l):
            bool = False
            print(k)
            break
    elif k**l == n:
        if d(k,l):
            bool = False
            print(k)
            break
    l -= 1

if bool:
    print(-1)
