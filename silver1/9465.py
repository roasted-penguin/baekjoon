import sys
T = int(sys.stdin.readline())
for _ in range(T):
  n = int(sys.stdin.readline())
  arr1 = list(map(int,sys.stdin.readline().split()))
  arr2 = list(map(int,sys.stdin.readline().split()))
  maxarr1 = [0] + [arr1[0]]
  maxarr2 = [0] + [arr2[0]]
  for i in range(1,n):
    maxarr1.append(max(maxarr2[i-1],maxarr2[i])+arr1[i])
    maxarr2.append(max(maxarr1[i-1],maxarr1[i])+arr2[i])
  print(max(maxarr1[-1],maxarr2[-1]))
