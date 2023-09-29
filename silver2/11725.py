import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
queue = deque()
for _ in range(N-1):
  a, b = map(int,sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(2,N+1):
  if len(graph[i])==1:
    queue.append(i)

res = [0 for _ in range(N+1)]
while queue:
  node = queue.popleft() #7
  res[node] = graph[node].pop() #4
  graph[res[node]].remove(node) #4에서 7pop
  if len(graph[res[node]])==1 and res[node]!=1:
    queue.append(res[node])

for i in range(2,N+1):
  print(res[i])
