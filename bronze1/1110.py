N = input()
num = N
res = 1
while True:
    x = 0
    for i in range(len(num)):
        x += int(num[i])
    y = num[-1]
    x = str(x)
    T = int(x[-1])+10*int(y)
    if T == int(N):
        break
    num = str(T)
    res += 1
print(res)
