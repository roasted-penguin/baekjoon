N = int(input())
ans = 1

if N != 0:
  for i in range(N):
    ans *= i+1

print(ans)
