N, M = map(int,input().split())
arr = [[[] for _ in range(26)] for _ in range(26)]

for _ in range(N):
    sen = input()
    num1 = ord(sen[0])-97
    num2 = ord(sen[-1])-97
    arr[num1][num2].append(sen)

cnt = 0
for _ in range(M):
    sen = input()
    num1 = ord(sen[0])-97
    num2 = ord(sen[-1])-97
    if sen in arr[num1][num2]:
        cnt += 1
print(cnt)
