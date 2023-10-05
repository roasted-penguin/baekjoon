import sys
import copy

N, M = map(int,sys.stdin.readline().split())
now_x, now_y, d = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
# 반시계
dx = [-1,0,1,0]
dy = [0,1,0,-1]

cnt = 1

visited[now_x][now_y] = True
x = now_x
y = now_y
while True:
  #청소한다
  first_visit = False
  if not visited[x][y]:
    cnt += 1
    visited[x][y] = True
  #주변 청소되지 않은 빈칸이 있는지 확인한다
  flag = False
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if not visited[nx][ny] and graph[nx][ny]==0:
      flag = True
      break
  #2 b : back
  if not flag:
    bd = (d+2) % 4
    bx = x + dx[bd]
    by = y + dy[bd]
    if bx < 0 or bx >= N or by < 0 or by >= M:
      continue
    if graph[bx][by]==1:
      break
    if graph[bx][by] == 0:
      x = bx
      y = by
      continue
  #3 n : new
  if flag:
    for i in range(1,5):
      nd = (d-i) % 4
      nx = x + dx[nd]
      ny = y + dy[nd]
      if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue

      if graph[nx][ny]==0 and not visited[nx][ny]:
        x = nx
        y = ny
        d = nd
        break
print(cnt)
