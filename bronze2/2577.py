"""
1. 0으로 초기화된 크기 n인 list 만들기 : list = [0 for i in range(n)]
"""
A = int(input())
B = int(input())
C = int(input())

ans = A*B*C
answer = str(ans)
thelist = [0 for i in range(10)]

for i in range(len(answer)):
  thelist[int(answer[i])] += 1

for j in range(len(thelist)):
  print(thelist[j])
