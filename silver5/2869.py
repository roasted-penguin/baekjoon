import math
A, B, V = map(int, input().split())# V < A + X*(A-B)       X > (V-A)/(a-B)
X = int(math.ceil((V-A)/(A-B)))+1
print(X)
