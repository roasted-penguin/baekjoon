def modpow(x, n, mod):
    res = 1;
    while n > 0:
        # 최하위 비트가 서있을 경우에 x ^ (2^i)를 곱한다.
        if n & 1:
            res = res * x % mod
        x = x * x % mod
        n //= 2
    return res

N, R = map(int,input().split())

if R > (N//2):
    R = N - R

ans = 1
for i in range(R):
    ans *= N-i
    if ans >1000000007:
        ans = ans%1000000007
    # print("i ",ans)

for j in range(R):
    ans *= modpow(j+1,1000000005,1000000007)
    if ans > 1000000007:
        ans = ans%1000000007
print(ans)
