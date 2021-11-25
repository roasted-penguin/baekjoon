def gcd(x,y):
  if x%y == 0:
    return y
  else:
    return gcd(y,x%y)

a, b = map(int,input().split())
G = gcd(a,b)
num = ""
for i in range(G):
  num += "1"
print(num)
