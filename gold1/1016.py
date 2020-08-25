import math

Min, Max = map(int,input().split())
sqrtMax = int(math.sqrt(Max))

prime = [2]
for i in range(3,sqrtMax,2):
    boolean = True
    length = len(prime)
    for j in range(length):
        if i%prime[j] == 0:
            boolean = False
            # print('break')
            break
        if math.sqrt(i) <= prime[j]:
            # print('leak')
            break
    if boolean:
        prime.append(i)

print(prime)
            

"""
def isprime(N):
  if N > 1:
    for i in range(N-2): #2~N-1 : N-2번loop
      if N % (i+2) == 0:
        return False
    return True
  else:
    return False

primenums = []
for i in range(2,sqrtMax):
  if isprime(i):
    primenums.append(i)
"""

# for i in range(2,) int(math.sqrt(Max))
