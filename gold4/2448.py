import math
import copy
N = int(input())
N //= 3
arr = [[' ',' ','*',' ',' '],[' ','*',' ','*',' '],['*','*','*','*','*']]
N = int(math.log(N,2))

x = 3
y = 5

for i in range(N):
  carr = copy.deepcopy(arr)
  newarr = []
  appendarr = [' ' for _ in range(3*(2**i))]
  for j in range(3*(2**i)):
    newarr.append(appendarr+arr[j]+appendarr)

  for j in range(3*(2**i)):
    newarr.append(arr[j]+[' ']+arr[j])

  arr = newarr[:]


def print_arr(arr):
  lenarr = len(arr)
  for i in range(lenarr):
    for j in range(2*lenarr-1):
      print(arr[i][j],end='')
    print()

print_arr(arr)
