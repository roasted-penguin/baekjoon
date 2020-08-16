N, K = map(int,input().split())
ans = 1
if K != 0:
  for i in range(N):
    ans *= N-i
  for j in range(K):
    ans //= K-j
  for k in range(N-K):
    ans //= N-K-k
print(ans)
