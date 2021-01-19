#않이 외틇림?
from collections import deque
import math
    
def func(now,topower,index,sign):
    if index == 1:
        now *= topower
        now = now%C
    if sign == 0:
        now = math.pow(now,2)
    now = int(now%C)
    return now
A, B, C = map(int,input().split())
binary = deque()
while B > 0:
    if B%2 == 1:
        binary.appendleft(1)
    else:
        binary.appendleft(0)
    B //= 2
result = 1
sign = 0
lenbin = len(binary)
for i in range(lenbin):
    if i == lenbin-1:
        sign = 1
    result = func(result,A,binary[i],sign)
print(result)
