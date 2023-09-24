import sys
arr = list(map(str,sys.stdin.readline().rstrip().split('-')))
res = 0
for i in range(len(arr)):
  item = arr[i]
  tosum = list(map(str,item.split('+')))
  res2 = 0
  for item2 in tosum:
    res2 += int(item2)
  if i==0:
    res += res2
  else:
    res -= res2
print(res)
