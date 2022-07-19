from collections import deque

N, M, V = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(v,visited):
    visited.append(v)
    print(v, end=' ')

    for i in range(N+1):
        if graph[v][i] == 1 and (i not in visited):
            dfs(i,visited)

def bfs(v,visited):
    visited.append(v)
    print(v, end=' ')

    q = deque()
    q.append(v)

    while q:
        v = q.popleft()
        for i in range(N+1):
            if graph[v][i] == 1 and (i not in visited):
                q.append(i)
                visited.append(i)
                print(i, end=' ')


visited = deque()
dfs(V,visited)

print()

visited = deque()
bfs(V,visited)
