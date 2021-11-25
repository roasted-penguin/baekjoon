num = int(input())
arr = list(map(int,input().split()))
ans = 0
for i in range(5):
  if arr[i] == num:
    ans += 1
print(ans)
