N, R = map(int,input().split())
ans = 1
for i in range(R):
    ans *= N-i
    if ans >1000000007:
        ans = ans%1000000007
    print("i ",ans)

for j in range(R):
    for k in range(1000000005): #idea임 
        ans *= j+1
        if ans > 1000000007:
            ans = ans%1000000007
print(ans)
