N, L = map(int,input().split())
tf = False
k = 0
while L <= 100:
    if L%2:#odd
        k = N//L
        if N%L == 0:
            if (k - L//2) >= 0:
                tf = True
                k = k - L//2
                break
    else:#even
        k = (N//(L//2))//2
        if N%(L//2)==0 and (N//(L//2))%2 == 1:
            if k - (L//2 - 1) >= 0:
                tf = True
                k = k - (L//2 - 1)
                break
    L += 1

if tf == False:
    print(-1)
else:
    for i in range(L):
        print(k,end=' ')
        k += 1
