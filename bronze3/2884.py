hour, minute = map(int,input().split())

if minute < 45:
  minute += 15
  if hour == 0:
    hour = 23
  else:
    hour -= 1
else:
  minute -= 45

print(hour,minute)
