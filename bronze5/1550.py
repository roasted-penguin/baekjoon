num = input()
length = len(num)
ans = 0
for i in range(length):
  st = num[length-1-i]
  if 65 <= ord(st) and ord(st) <=70:
    ans += (ord(st)-55)*(16**i)
  else:
    ans += int(st)*(16**i)

print(ans)
