import math

T = int(input())
for i in range(T):
  x1, y1, r1, x2, y2, r2 = map(int,input().split())
  d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
  if x1 == x2 and y1 == y2:#두 좌표가 같음
    if r1 == r2: # 같은원
      print(-1)
    else:
      print(0)
  else:
    if abs(r1-r2) < d and d < r1 + r2: # 두점이 접함
      print(2)
    elif abs(r1-r2) == d or r1+r2 == d: # 순서대로 내접,외접
      print(1)
    else: # 외부 r1+r2 < d 내부 d < abs(r1-r2)
      print(0)
