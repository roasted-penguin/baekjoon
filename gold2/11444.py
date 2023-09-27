N = int(input())
if N == 1 or N==2:
  print(1)
else:
  binary = []
  while N > 0:
    binary.append(N%2)
    N //= 2

  
  arr = [1,1,0]
  binary.pop()
  while binary:
    n = binary.pop()
    x0, x1, x2 = -1, -1, -1
    if n==1:
      x1 = (arr[0]**2+arr[1]**2) % 1000000007
      x2 = (arr[1]**2+2*arr[1]*arr[2]) % 1000000007
      x0 = (x1+x2) % 1000000007
    if n==0:
      x1 = (arr[1]**2+2*arr[1]*arr[2]) % 1000000007
      x2 = (arr[1]**2+arr[2]**2) % 1000000007
      x0 = (x1+x2) % 1000000007
    arr = [x0,x1,x2]
  
  
  print(arr[1])
