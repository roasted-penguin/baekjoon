T = int(input())
for i in range(T):
  N = int(input())
  arr = list(map(int,input().split()))
  cnt = 0
  for j in range(N):
    cnt += arr[j]
  print(cnt)
