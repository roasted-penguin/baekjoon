def gcd(a,b):
  while b != 0:
    num = a%b
    a = b
    b = num
  return a

def lcm(a,b):
  return a*b//gcd(a,b)

N = int(input())
for i in range(N):
  num1, num2 = map(int,input().split())
  print(lcm(num1,num2))
