#1번코드
N = int(input())

arr = [0,True,False,True]

for i in range(4,N+1):
  if not arr[i-1] or not arr[i-3] or not arr[i-4]:
    arr.append(True)
  else:
    arr.append(False)

for i in range(1,N+1):
  print(i,arr[i])
if arr[N]:
  print('SK')
else:
  print('CY')
  
#2번코드
"""    
전수조사결과
T = SK 
F = CY
TFTTTTFTFT
TTTFTFTTTT
FTFTTTTFTF
TTTTFTFTTT
TFTFTTTTFT
F : 2 7 9 14 16 21 23 28 30 35 37 42 44 49 51
F조건 : 7k or 7k+2 (k>=0)
"""
N = int(input())
if N%7 == 2 or N%7 == 0:
  print('CY')
else:
  print('SK')
