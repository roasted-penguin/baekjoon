N, M = map(int,input().split())

def dfs(n,arr):
  if len(arr)==M:
    print_arr(arr)
    return
  for i in range(n,N+1):
    arr.append(i)
    dfs(i,arr)
    arr.pop()
  

def print_arr(arr):
  for item in arr:
    print(item,end=' ')
  print()
  
dfs(1,[])
