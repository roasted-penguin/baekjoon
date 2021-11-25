"""
#1. 배열

N = int(input())
A = []
ansarr =[0 for i in range(N+1)]
for i in range(1,N+1):
  val = int(input())
  count = 0
  for j in range(1,N+1):
    compare = ansarr[j]
    if count == val and compare == 0:
      ansarr[j] = i
      break
    if compare == 0:
      count += 1
  
for i in range(1,N+1):
  print(ansarr[i])
  
#2. stack 활용(pop)

N = int(input())
values = []
for i in range(N):
  values.append(i)
ansarr =[0 for i in range(N)]
for i in range(0,N):
  val = int(input())
  index = values.pop(val)
  ansarr[index] = i+1

  
for i in range(0,N):
  print(ansarr[i])
"""
