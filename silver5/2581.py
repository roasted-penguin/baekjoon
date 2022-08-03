import math
M = int(input())
N = int(input())
prime = [2]
for i in range(3,10001):
    isprime = True
    for j in range(2,int(math.sqrt(i))+1):
        if i % j == 0:
            isprime = False
            break
    if isprime:
        prime.append(i)

p = 0
l = len(prime)
ans = 0
min = 0
while p < l and prime[p] < M:
    p += 1

min = prime[p]
while p < l and prime[p] <= N:
    ans += prime[p]
    p += 1

if ans != 0:
    print(ans)
    print(min)
else:
    print(-1)
