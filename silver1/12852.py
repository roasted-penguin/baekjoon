N = int(input())
def make(X):
    arr = [0,0,1,1]
    arr2 = [[0],[1],[1,2],[1,3]]
    for i in range(4,X+1):
        m = 0
        if i % 2 == 0 and i % 3 == 0:
            if arr[i//2] >= arr[i//3]:
                if arr[i//3] >= arr[i-1]:
                    m = arr[i-1]
                    marr = arr2[i-1]
                else:
                    m = arr[i//3]
                    marr = arr2[i//3]
            else:
                if arr[i//2] >= arr[i-1]:
                    m = arr[i-1]
                    marr = arr2[i-1]
                else:
                    m = arr[i//2]
                    marr = arr2[i//2]
        elif i % 2 != 0 and i % 3 == 0:
            if arr[i//3] >= arr[i-1]:
                m = arr[i-1]
                marr = arr2[i-1]
            else:
                m = arr[i//3]
                marr = arr2[i//3]
        elif i % 2 == 0 and i % 3 != 0:
            if arr[i//2] >= arr[i-1]:
                m = arr[i-1]
                marr = arr2[i-1]
            else:
                m = arr[i//2]
                marr = arr2[i//2]
        else:
            m = arr[i-1]
            marr = arr2[i-1]
        arr.append(m+1)
        arr2.append(marr+[i])
    arr2[X].reverse()
    return [arr[X], arr2[X]]
ans = make(N)

print(ans[0])
for i in range(len(ans[1])):
    print(ans[1][i],end=' ')
