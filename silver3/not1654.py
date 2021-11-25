#시간초과

import math
K, N = map(int,input().split())
lan = []
S = 0

for i in range(K):
  num = int(input())
  lan.append(num)
  S += num
maximum = math.ceil(S)//N

ans = 0
for i in range(maximum,0,-1):
  wire = 0
  for j in range(K):
    wire += lan[j]//i
  if wire >= N:
    ans = i
    break
print(ans)
