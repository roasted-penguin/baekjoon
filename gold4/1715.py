import sys
import heapq
from heapq import heappush, heappop 

N = int(sys.stdin.readline())
heap = []
for _ in range(N):
  heappush(heap,int(sys.stdin.readline()))
  
res = 0
while len(heap) > 1:
  x = heappop(heap)
  y = heappop(heap)
  num = x + y
  res += num
  heappush(heap,num)
print(res)
