def isprime(N):
  if N > 1:
    for i in range(N-2): #2~N-1 : N-2번loop
      if N % (i+2) == 0:
        return False
    return True
  else:
    return False

N = int(input())

numbers = list(map(int,input().split()))
count = 0

for i in range(N):
  if isprime(numbers[i]):
    count += 1

print(count)
