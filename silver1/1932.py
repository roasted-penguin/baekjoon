N = int(input())

arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))

for i in range(N):
    for j in range(N-i-1):
        arr[N-i-2][j] = max(arr[N-i-1][j],arr[N-i-1][j+1]) + arr[N-i-2][j]

print(arr[0][0])
