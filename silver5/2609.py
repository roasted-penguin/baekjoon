"""
1. 최대공약수 : gcd
2. 최소공배수 : lcm
"""

def gcd(a,b):
  mod = a%b
  while mod != 0:
    a = b
    b = mod
    mod = a%b
  return b

def lcm(a,b):
  return a*b//gcd(a,b)

x, y = map(int,input().split())

print(gcd(x,y),lcm(x,y))
