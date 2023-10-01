import sys
import heapq
V, E = map(int,sys.stdin.readline().split())
INF = int(1e9)
K = int(sys.stdin.readline())

# graph : [node,weight]
graph = [[] for _ in range(V+1)]
# distances
distances = [INF for _ in range(V+1)]
distances[K] = 0

for _ in range(E):
  u, v, w = map(int,sys.stdin.readline().split())
  graph[u].append((v,w))

# pq : 최소힙(weight,node)
pq = [(0,K)]
while pq:
  weight_now, node_now = heapq.heappop(pq)
  for neighbor, weight in graph[node_now]:
    distance = weight_now + weight
    # distance 최소면 갱신
    if distance < distances[neighbor]:
      distances[neighbor] = distance
      heapq.heappush(pq,(distance,neighbor))


for i in range(1,V+1):
  if distances[i]==INF:
    print("INF")
  else:
    print(distances[i])
