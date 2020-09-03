T = int(input())

def gcd(x,y):
  if x%y == 0:
    return y
  else:
    return gcd(y,x%y)
    
def lcm(x,y,gcd):
  return int(x*y//gcd)
  
for i in range(T):
  a, b = map(int,input().split())
  G = gcd(a,b)
  L = lcm(a,b,G)
  print(L,G)
