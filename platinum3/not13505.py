import math
n = int(input())
num = list(map(int,input().split()))
num.sort()
num.reverse()
Bnum = num[0]
length = len(num)

binaries = list()
i = 0
while True:
    b = int(math.pow(2,i))
    if b > int(1e9):
        break
    binaries.append(b)
    i += 1
binaries.reverse()

i = 0
while True:
    if Bnum >= binaries[i]:
        binary = binaries[i]
        break
    i += 1
    
i = 0
ans = 0
while i < length and binary <= num[i]:
    inum = num[i]
    for j in range(i,length):
        compete = inum ^ num[j]
        ans = max(ans,compete)
    i += 1
print(ans)
