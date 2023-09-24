import sys
N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
res = 0
if N == 1:
  arr.sort()
  res = (arr[0]+arr[1]+arr[2]+arr[3]+arr[4])
else:
  set1 = min(arr)
  set2 = 10**9
  set3 = 10**9
  pairs2 = [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,5],[2,4],[2,5],[3,4],[3,5],[4,5]]
  pairs3 = [[0,1,2],[0,1,3],[0,2,4],[0,3,4],[1,2,5],[1,3,5],[2,4,5],[3,4,5]]
  
  for pair in pairs2:
    sum = 0
    for i in range(2):
      sum += arr[pair[i]]
    set2 = min(set2,sum)
    
  for pair in pairs3:
    sum = 0
    for i in range(3):
      sum += arr[pair[i]]
    set3 = min(set3,sum)
  if N == 2:
    res = 4*(set2+set3)
  else:
    mult1 = (N-2)*(5*N-6)
    mult2 = 8*N-12
    mult3 = 4
    res = set1*mult1 + set2*mult2 + set3*mult3
print(res)
