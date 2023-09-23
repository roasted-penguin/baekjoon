from itertools import combinations
import copy
from collections import deque

N, M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]

# 벽 세우는 경우의 수 : (N*M) C 3
combarr = []

for i in range(N):
  for j in range(M):
    combarr.append([i,j])

comb3 = list(combinations(combarr,3))

# 1. 벽만들기
def makewall(arr,comb3):
  result = 0
  for i in range(len(comb3)):
    flag = True
    graph = copy.deepcopy(arr)
    for j in range(3):
      if flag:
        x, y = comb3[i][j]
        if graph[x][y] != 0:
          flag = False
          continue
        graph[x][y] = 1
        
    if flag: 
      spread(graph)
      cntzero = countzero(graph)
      if cntzero > result:
        result = cntzero
  print(result)

# 2. 바이러스 증식
def spread(graph):
  queue = deque()
  for x in range(N):
    for y in range(M):
      if graph[x][y] == 2:
        queue.append([x,y])
        
  while queue:
    x, y = queue.popleft()
    if graph[x][y] == 2:
      dx = [0,0,1,-1]
      dy = [1,-1,0,0]
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if(nx < 0 or nx >= N or ny < 0 or ny >= M):
          continue
        if graph[nx][ny]==0:
          queue.append([nx,ny])
          graph[nx][ny] = 2
  
  
# 3. 0 갯수 세기
def countzero(graph):
  count = 0
  for i in range(N):
    for j in range(M):
      if graph[i][j]==0:
        count += 1
  return count

makewall(arr,comb3)
