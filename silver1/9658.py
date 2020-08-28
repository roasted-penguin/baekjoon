#1번코드
N = int(input())

arr = [0,False,True,False,True]

for i in range(5,N+1):
  if not arr[i-1] or not arr[i-3] or not arr[i-4]:
    arr.append(True)
  else:
    arr.append(False)

if arr[N]:
  print('SK')
else:
  print('CY')
  
#2번코드
N = int(input())
if N%7 == 1 or N%7 == 3:
  print('CY')
else:
  print('SK')
