N = input()
arr = [0 for _ in range(10)]
for i in range(len(N)):
    num = int(N[i])
    arr[num] += 1

if arr[0] == 0:
    print("-1")
else:
    sum = 0
    for i in range(10):
        sum += arr[i]*i
    if sum%3 == 0:
        k = 9
        sen = ""
        while k > -1:
            if arr[k] == 0:
                k -= 1
            else:
                sen += str(k)
                arr[k] -= 1
        print(sen)
    else:
        print("-1")
