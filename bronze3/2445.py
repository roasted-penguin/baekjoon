N = int(input())
for i in range(1,2*N):
    ans = ""
    star = -1*abs(N-i)+N
    space = 2*(N-star)
    ans += star*"*"
    ans += space*" "
    ans += star*"*"
    print(ans)
