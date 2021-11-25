N = input()
length = len(N)
boolean = 0
for i in range(1,length):
    a = N[0:i]
    b = N[i:]
    pA = 1
    pB = 1
    for j in range(len(a)):
        pA *= int(a[j])
    for j in range(len(b)):
        pB *= int(b[j])
    if pA == pB:
        print("YES")
        boolean = 1
        break
if boolean == 0:
    print("NO")
