arr = [0,1,2,4]

def initializearr(mx):
  if mx >= 4 : 
    for i in range(4,mx+1):
      arri = arr[i-1] + arr[i-2] + arr[i-3]
      arri = arri % 1000000009
      arr.append(arri)
  return arr
  
def f(x,arr):
  res = arr[x]
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
