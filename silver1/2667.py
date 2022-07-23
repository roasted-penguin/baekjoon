import sys

N = int(input())
graph = []
for _ in range(N):
    sen = sys.stdin.readline()
    arr = []
    for i in range(N):
        arr.append(int(sen[i]))
    graph.append(arr)

visited = [[False] * N for _ in range(N)]

def dfs(x,y,visited):
    global cnt
    cnt += 1
    visited[x][y] = True
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if graph[nx][ny] == 1 and not visited[nx][ny]:
            dfs(nx,ny,visited)
total = 0
cnt = 0
houses = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt = 0
            dfs(i,j,visited)
            houses.append(cnt)
            total += 1
print(total)
houses.sort()
for i in range(len(houses)):
    print(houses[i])
