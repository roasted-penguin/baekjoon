N = int(input())
ans = max(0,N-9*6)
while True:
    copy = ans
    S = 0
    while copy > 0:
        S += copy%10
        copy //= 10
    if ans + S == N:
        break
    if ans == N:
        ans = 0
        break
    ans += 1
print(ans)
