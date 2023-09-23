import sys
# dfs 재귀 한도 늘려준다
sys.setrecursionlimit(10 ** 9)
# N커지면 input에서 시간초과 터진다
N, M ,R = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

# 그래프 세팅
for _ in range(M):
  x, y = map(int,sys.stdin.readline().split())
  graph[x].append(y)
  graph[y].append(x)
  
# 오름차순 정렬
for node in graph:
  node.sort()


order = 1
res = [0 for _ in range(N+1)]
# dfs
def dfs(graph,R,visited):
  global order
  res[R] = order
  order += 1
  visited[R] = True
  for node in graph[R]:
    if not visited[node]:
      dfs(graph,node,visited)

visited = [False for _ in range(N+1)]
dfs(graph,R,visited)

# 출력
for i in range(1,N+1):
  print(res[i])
