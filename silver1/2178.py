import sys
from collections import deque
N, M = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(N)]

queue = deque()
queue.append([0,0])
dx = [0,0,-1,1]
dy = [1,-1,0,0]
visited = [[False for _ in range(M)] for _ in range(N)]
visited[0][0] = True
while queue:
  x,y = queue.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
      continue
    if not visited[nx][ny] and graph[nx][ny]!=0:
      if graph[nx][ny] < graph[x][y] + 1:
        graph[nx][ny] = graph[x][y] + 1
      queue.append([nx,ny])
      visited[nx][ny] = True
print(graph[N-1][M-1])
