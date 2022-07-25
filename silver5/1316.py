N = int(input())
cnt = 0
for _ in range(N):
    sen = input()
    checker = [False for _ in range(26)]
    c = 1
    last = 27
    for i in range(len(sen)):
        x = ord(sen[i])-97
        if not last == x:
            if not checker[x]:
                checker[x] = True
            else:
                c = 0
                break
        last = x
    cnt += c
print(cnt)
