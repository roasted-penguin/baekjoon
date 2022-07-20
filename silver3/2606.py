#1260.py의 dfs(), bfs()
from collections import deque


N = int(input())
M = int(input())

graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(v,visited,ruined):
    visited.append(v)
    ruined += 1

    for i in range(N+1):
        if graph[v][i] == 1 and (i not in visited):
            ruined += dfs(i,visited,0)
    return ruined

def bfs(v,visited,ruined):
    visited.append(v)
    ruined += 1

    q = deque()
    q.append(v)

    while q:
        v = q.popleft()
        for i in range(N+1):
            if graph[v][i] == 1 and (i not in visited):
                q.append(i)
                visited.append(i)
                ruined += 1
    return ruined


visited = deque()
print(dfs(1,visited,0)-1) #1은 포함 x
# or
#print(bfs(1,visited,0)-1) #1은 포함 x
