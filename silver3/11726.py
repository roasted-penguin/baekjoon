n = int(input())

do = [0,1,2]
for i in range(3,n+1):
  do.append((do[i-1] + do[i-2])%10007)

print(do[n])
