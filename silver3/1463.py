#DP

N = int(input())
def make(X):
  arr = [0,0,1,1]
  for i in range(4,X+1):
    if i % 2 == 0 and i % 3 == 0:
      arr.append(min(arr[i//2],arr[i//3],arr[i-1]) + 1)
    elif i % 2 != 0 and i % 3 == 0:
      arr.append(min(arr[i//3],arr[i-1]) + 1)
    elif i % 2 == 0 and i % 3 != 0:
      arr.append(min(arr[i//2],arr[i-1]) + 1)
    else:
      arr.append(arr[i-1] + 1)
  return arr[X]

print(make(N))
