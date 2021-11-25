def gcd(a,b):
  mod = a%b
  while mod != 0:
    a = b
    b = mod
    mod = a%b
  return b

def lcm(a,b):
  return a*b//gcd(a,b)

a1, a2 = map(int,input().split())
b1, b2 = map(int,input().split())
c2 = a2*b2
c1 = a2*b1 + b2*a1
g = gcd(c1,c2)
c1 //= g
c2 //= g
print(c1,c2)
