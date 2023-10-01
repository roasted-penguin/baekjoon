import sys
N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

up = [1 for _ in range(N)]
down = [1 for _ in range(N)]

# 시간복잡도 : O(N^2), N=1000
for i in range(N):
  for j in range(i):
    if arr[i] > arr[j]:
      up[i] = max(up[i],up[j]+1)
    if arr[N-1-i] > arr[N-1-j]:
      down[N-1-i] = max(down[N-1-i],down[N-1-j]+1)

sum = []
for i in range(N):
  sum.append(up[i]+down[i]-1)
print(max(sum))
