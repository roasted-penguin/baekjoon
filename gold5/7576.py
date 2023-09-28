import sys
from collections import deque
import copy

M, N = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
queue = deque()
new_queue = deque()
cnt = 1
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 1. graph 순회, visited = True, queue에 일 수 넣기
for i in range(N):
  for j in range(M):
    if graph[i][j] == -1:
      visited[i][j] = True
    if graph[i][j] == 1:
      queue.append([i,j])
      visited[i][j] = True
# 2. while queue: 루프
while queue:
  node = queue.pop()
  x = node[0]
  y = node[1]
  # 2-1.
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
      continue
    if not visited[nx][ny]:
      visited[nx][ny] = True
      graph[nx][ny] = cnt
      new_queue.append([nx,ny])
  # 2-2-1. if new_queue:queue를 new_queue로 변경
  if not queue:
    if new_queue:
      queue = copy.deepcopy(new_queue)
      new_queue = deque()
      cnt += 1
    # 2-2-2. else: 끝
    else:
      break


# 3. 0 없으면 루프횟수(cnt), 0 하나라도 있으면 -1 출력
flag = False
for i in range(N):
  for j in range(M):
    if graph[i][j] == 0:
      flag = True
      break

if flag:
  print(-1)
else:
  print(cnt-1)
