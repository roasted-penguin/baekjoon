from collections import deque
import math
A, B, C = map(int,input().split())
arr = []
while B > 0:
    arr.append(B%2)
    B = B//2

X = 0
res = 1
for i in range(len(arr)):
    if i==0:
        X = A
        X = X%C
    else:
        X = X*X
        X = X%C
    if arr[i]:
        res = res * X
    res = res%C
print(res)
