import math
for i in range(1,10001):
    bool = True
    l = int(math.log10(i))
    m = 9*l + int(i//math.pow(10,l))
    for j in range(1,m+1):
        num = i-j
        sum = num
        while(num>0):
            sum += num%10
            num //= 10
        if sum == i:
            bool = False
            break
    if bool:
        print(i)
