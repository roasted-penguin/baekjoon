def minusbinary(n):
    b = 1
    bin = ""
    if n == 0:
        return "0"
    else:
        while n != 0:
            if n%2==0:
                bin = "0" + bin
            else:
                bin = "1" + bin
                n -= b
            b = b * (-1)
            n = n // 2
        return bin

N = int(input())
print(minusbinary(N))
