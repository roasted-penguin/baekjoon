n = int(input())
store = [1]
if n == 0:
    print(1)
else:
    for i in range(1,n+1):
        num = 0
        for j in range(i):
            num += store[j]*store[i-j-1]
        store.append(num)
    print(store[n])
