def method(n):
  if n == 1:
    return 1
  elif n == 2:
    return 2
  elif n == 3:
    return 4
  else:
    return method(n-3) + method(n-2) + method(n-1)
    
T = int(input())
for i in range(T):
  number = int(input())
  print(method(number))
