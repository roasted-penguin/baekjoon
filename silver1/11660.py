import sys
N, M = map(int,sys.stdin.readline().split())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

sumarr = [[0 for _ in range(N+1)]]
#가로로 더하기
for i in range(N):
  toappend = [0]
  num = 0
  for j in range(N):
    num += arr[i][j]
    toappend.append(num)
  sumarr.append(toappend)
#세로로 더하기
for i in range(1,N+1):
  for j in range(1,N+1):
    sumarr[i][j] += sumarr[i-1][j]
  
for _ in range(M):
  x1, y1, x2, y2 = map(int,sys.stdin.readline().split())
  # 겹치는부분 더해준다
  res = sumarr[x2][y2] - sumarr[x1-1][y2] - sumarr[x2][y1-1] + sumarr[x1-1][y1-1]
  print(res)
