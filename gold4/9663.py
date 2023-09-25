import sys
# 주석처리안하면 시간초과뜬다 
# sys.setrecursionlimit(10**5)
N = int(sys.stdin.readline())

arr = []

visited = [False for _ in range(N)]
cnt = 0
def dfs(level):
  if level == N:
    global cnt
    cnt += 1
    return
  for i in range(N):
    # 이미 방문한 곳이면 promising 중복검사 횟수를 줄인다
    if visited[i]:
      continue
    if promising(level,i): 
      arr.append(i)
      visited[i] = True
      dfs(level+1)
      arr.pop()
      visited[i] = False
  return
    
  
def promising(level,i):
  for j in range(level):
    if abs(level-j) == abs(arr[j]-i):
      return False
  return True

dfs(0)
print(cnt)
