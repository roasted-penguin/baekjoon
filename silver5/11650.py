N = int(input())
arr = []
for i in range(N):
  arr.append(list(map(int,input().split())))

arr = sorted(arr)

for i in range(N):
  print(arr[i][0],arr[i][1])
