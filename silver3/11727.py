def com(N,K):
  ans = 1
  if K != 0:
    for i in range(N):
      ans *= N-i
    for j in range(K):
      ans //= K-j
    for k in range(N-K):
      ans //= N-K-k
  return ans

n = int(input())

ans = 0
r = n
loop = 0
while r >= 0:
  ans += com(n,r)*2**loop
  ans %= 10007
  loop += 1
  n -= 1
  r -= 2
print(ans)
