A, B = map(int,input().split())

cnt = 0
while B > A:
    if (B-1)%10==0:
        B = (B-1)//10
        cnt += 1
    elif B%2==0:
        B //= 2
        cnt += 1
    else:
        break
if B == A:
    print(cnt+1)
else:
    print(-1)
