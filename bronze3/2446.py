N = int(input())
for i in range(1,2*N):
    ans = ""
    space = -1*abs(N-i)+N-1
    star= 2*(N-space)-1
    ans += space*" "
    ans += star*"*"
    print(ans)
