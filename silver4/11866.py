N, K = map(int,input().split())
arr = []
ans = "<"
for i in range(N):
  arr.append(i+1)

now = 0
for i in range(N):
  now = (now+K-1)%len(arr)
  ans = ans + str(arr.pop(now))
  if i != N-1:
    ans = ans + ", "
ans += ">"
print(ans)
