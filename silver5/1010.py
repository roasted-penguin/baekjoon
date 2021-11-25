def comb(a,b):
    ans = 1
    for i in range(a):
        ans *= a-i
    for i in range(b):
        ans //= i+1
    for i in range(a-b):
        ans //= a-b-i
    return ans
N = int(input())
for _ in range(N):
    r, n = map(int,input().split())
    print(comb(n,r))
