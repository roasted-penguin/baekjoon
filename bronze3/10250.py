"""
1. 우선순위 : 거리 > 높이
"""
import math
def alloc(h,w,n):
    room = math.ceil(n/h)
    if room < 10:
        room = '0' + str(room)
    else:
        room = str(room)

    floor = n % h
    if floor == 0:
        floor = str(h)
    else:
        floor = str(floor)
        
    return floor+room



T = int(input())

for i in range(T):
  H, W, N = map(int,input().split())
  roomname = alloc(H,W,N)
  print(roomname)
