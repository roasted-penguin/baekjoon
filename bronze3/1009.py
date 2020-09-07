T = int(input())

for i in range(T):
  a, b = map(int,input().split())
  if a % 10 == 0:
    print(10)
  else:
    if not b%4:
      k = 4
    else:
      k = b%4
    num = 1
    for j in range(k):
      num *= a
      num %= 10
    print(num)
