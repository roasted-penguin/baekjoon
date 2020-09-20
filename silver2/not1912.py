N = int(input())
arr = list(map(int,input().split()))
Sarr = []
S = 0

for i in range(N):
  S += arr[i]
  Sarr.append(S)

m = Sarr[0]
for i in range(N):
  for j in range(i,N):
    t = Sarr[j] - Sarr[i]
    m = max(m,t)

print(m)
