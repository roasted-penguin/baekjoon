N, M = map(int,input().split())
arr = list(map(int,input().split()))

num = 0
A = []
for i in range(len(arr)):
    num += arr[i]
    A.append(num)


x = 0
y = 0
cnt = 0
for i in range(N):
    if A[i]==M:
        cnt += 1
while x<N and y<N:
    cal = A[y]-A[x]
    if cal == M:
        #print("Goal",x,y)
        cnt += 1
        if x+1 < y:
            x += 1
        else:
            x += 1
            y += 1
    elif cal > M:
        if x+1 < y:
            x += 1
        else:
            x += 1
            y += 1
    else:
        y += 1
print(cnt)
'''
1 4 6 9 11 12 15 18
2
1 4 붙어있으면 x옮기기
4 6 만족하므로
6 9
9 11
11 12 M보다 작으므로 y옮기기
11 15 M보다 크고 안붙어있으므로 x옮기기
12 15 M보다 크고 붙어있으므로 x옮기기 x==y이므로 y
15 18
'''
