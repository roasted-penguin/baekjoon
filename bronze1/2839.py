N = int(input())
k5 = 0
k3 = 0
k5 += N//5
remain = N%5
boolean = True
while remain%3 != 0:
  k5 -= 1
  if k5 < 0:
    boolean = False
    break
  remain += 5
if boolean:
  k3 += remain//3
  print(k5+k3)
else:
  print(-1)
