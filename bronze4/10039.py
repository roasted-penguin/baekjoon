S = 0
for i in range(5):
  num = int(input())
  if num < 40:
    S += 40
  else:
    S += num
print(S//5)
