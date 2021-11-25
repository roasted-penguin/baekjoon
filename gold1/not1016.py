import math

Min, Max = map(int,input().split())
sqrtMax = int(math.sqrt(Max))
            
def PrimeByEra(n):
  a = [False,False] + [True]*(n-1)
  primes=[]

  for i in range(2,n+1):
    if a[i]:
      primes.append(i)
      for j in range(2*i, n+1, i):
          a[j] = False
  return primes

# 1. 에라토스테네스의 체 알고리즘 이용, sqrt(Max)까지의 소수리스트 구한다
prime = PrimeByEra(sqrtMax)
# print(prime)

# 2. Min부터 Max까지 loop: 소수리스트안에 있는 모든 소수에대해 소인수분해한다.
ans = 0

for i in range(Min,Max+1):
  num = i
  listp = list(prime) #깊은복사. listp = prime으로하면 얕은복사로, listp에 하는 명령이 prime에도 적용됨.
  boolean = True
  # print(i,listp)
  while listp:
    if num%(listp[-1]**2) == 0:
      boolean = False
      break
    else:
      listp.pop()
  if boolean:
    ans += 1

print(ans)
