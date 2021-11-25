N = int(input())

num = 1
ans = 0
for i in range(1,N+1):
    num *= i
    while num%10 == 0:
        num //= 10
        ans += 1
    
print(ans)
