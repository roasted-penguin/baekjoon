from collections import deque

N, M, V = map(int,input().split())
# dfs:stack bfs:queue
graph = list(list(0 for _ in range(N+1)) for _ in range(N+1))
for i in range(1,N+1):
    graph[i][i] = 1
for _ in range(M):
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

#dfs
g = deque(i for i in range(1,N+1))
g.remove(V)
print(g)
visited = list()
stack = list()
while True:
    visited.append(V)
    for i in range(1,N+1):
        if V != i and graph[V][i] == 1:
            graph[V][i] = 0
            graph[i][V] = 0
            g.remove(i)
            stack.append(i)
            print(0,g,visited,stack)
    if stack:
        thenode = stack.pop()
        visited.append(thenode)
        print(1,g,visited,stack)
    if g:
        V = g.popleft()
    else:
        break
print(visited)

#bfs
