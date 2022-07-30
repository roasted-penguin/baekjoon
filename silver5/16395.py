def fac(n):
    ans = 1
    for i in range(1,n+1):
        ans *= i
    return ans
def comb(n,k):
    ans = int(fac(n)/fac(n-k)/fac(k))
    return ans
n, k = map(int,input().split())
print(comb(n-1,k-1))
