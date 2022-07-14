arr = [[0,0,0],[1,0,0],[0,1,0],[1,1,1]]

def initializearr(mx):
  if mx >= 4 : 
    for i in range(4,mx+1):
      arri = []
      for j in range(3):
        if j == 0:
          k = (arr[i-1][1] + arr[i-1][2])%1000000009
        elif j == 1:
          k = (arr[i-2][0] + arr[i-2][2])%1000000009
        else:
          k = (arr[i-3][0] + arr[i-3][1])%1000000009
        arri.append(k)
      arr.append(arri)
  return arr
  
def f(x,arr):
  res = arr[x][0] + arr[x][1] + arr[x][2]
  res = res%1000000009
  print(res)


  
T = int(input())
mx = 0
arr2 = []
for i in range(T):
  n = int(input())
  if mx < n:
    mx = n
  arr2.append(n)

initializearr(mx)
for i in range(T):
  num = arr2[i]
  f(num,arr)
