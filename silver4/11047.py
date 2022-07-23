N, K = map(int,input().split())
coin = []
for _ in range(N):
    coin.append(int(input()))
coin.reverse()

res = 0
i = 0
while K!=0:
    num = K // coin[i]
    K = K%coin[i]
    res += num
    i += 1
print(res)
