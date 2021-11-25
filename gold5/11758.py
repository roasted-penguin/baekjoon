x1, y1 = map(int,input().split())
x2, y2 = map(int,input().split())
x3, y3 = map(int,input().split())
v1x = x2 - x1
v1y = y2 - y1
v2x = x3 - x2
v2y = y3 - y2
cross = v1x*v2y - v2x*v1y
if cross > 0: # 외적 양수 -> 반시계
  print(1)
elif cross < 0:# 외적 음수 -> 시계
  print(-1)
else:# 외적 0 -> 일직선
  print(0)
