N = int(input())
arr = list(map(int,input().split()))
arr.sort()
res = 0
time = 0
t = 0
for i in range(len(arr)):
    t = arr[i]
    time += t
    res += time
print(res)
