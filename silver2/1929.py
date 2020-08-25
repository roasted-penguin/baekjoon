# 소수리스트를 가장 최적으로 구하는방법 : 에라토스테네스의 체 알고리즘

def PrimeByEra(n):
  a = [False,False] + [True]*(n-1)
  primes=[]

  for i in range(2,n+1):
    if a[i]:
      primes.append(i)
      for j in range(2*i, n+1, i):
          a[j] = False
  return primes

M, N = map(int,input().split())
prime = PrimeByEra(N)

while prime[0] < M:
  prime.pop(0)
  
for i in range(len(prime)):
  print(prime[i])
        print(i)


