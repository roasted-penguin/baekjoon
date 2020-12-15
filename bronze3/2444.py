N = int(input())
for i in range(1,2*N):
    ans = ""
    space = abs(N-i)
    star = 2*(N-space)-1
    ans += space*" "
    ans += star*"*"
    print(ans)
