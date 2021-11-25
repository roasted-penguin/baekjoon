N = int(input())
M = int(input())
sen = input()

length = 2*N + 1
Pn = "I"
ans = 0

for i in range(N):
    Pn += "OI"
    
for i in range(len(sen)-length):
    if Pn == sen[i:i+length]:
        ans += 1
print(ans)
