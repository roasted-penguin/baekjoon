N, M = map(int,input().split())
board = []

def coloring(array,row,col,firstcolor):
  count = 0
  for i in range(8):
    for j in range(8):
      if (i+j)%2:
        if array[row+i][col+j]==firstcolor:
          count += 1
      else:
        if array[row+i][col+j]!=firstcolor:
          count += 1
  return count

for i in range(N):
  board.append(input())

ans = 8*8
for i in range(N-8+1):
  for j in range(M-8+1):
    W = coloring(board,i,j,'W')
    B = coloring(board,i,j,'B')
    if W > B:
      ans = min(ans,B)
    else:
      ans = min(ans,W)

print(ans)
