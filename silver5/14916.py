n = int(input())
ans = 0

ans += n//5
n %= 5
if ans > 0 and n%2==1:
  n += 5
  ans -= 1
  ans += n//2
elif ans == 0 and n%2==1:
  ans = -1
else:
  ans += n//2
print(ans)
