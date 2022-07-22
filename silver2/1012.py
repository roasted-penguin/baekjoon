import sys
sys.setrecursionlimit(10000)
def dfs(x,y,visited):
    visited[x][y] = True
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= M or ny >=N:
            continue
        if graph[nx][ny] == 1 and not visited[nx][ny]:
            dfs(nx,ny,visited)
'''
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
'''

T = int(input())
for _ in range(T):
    M, N, K = map(int,input().split())
    graph = [[0] * N for _ in range(M)]
    for _ in range(K):
        a, b = map(int,input().split())
        graph[a][b] = 1
    visited = [[False] * N for _ in range(M)]
    cnt = 0

    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1 and not visited[i][j]:
                cnt += 1
                dfs(i,j,visited)
    print(cnt)
