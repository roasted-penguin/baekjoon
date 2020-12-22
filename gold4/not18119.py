#시간초과
N, M = map(int,input().split())
word = [[0 for _ in range(27)] for _ in range(N)]#27번째 인덱스는 필요한 잊은 알파벳 수 의미
for i in range(N):
    w = input()
    for j in range(len(w)):
        word[i][ord(w[j])-97] = 1
remember = N
for i in range(M):
    what, order = map(str,input().split())
    odr = ord(order)-97
    if what == '1':
        for j in range(N):
            if word[j][odr] == 1:
                word[j][odr] = -1#-1은 잊어버린 필요 구성요소 의미
                if word[j][26] == 0:
                    remember -= 1
                word[j][26] += 1
    if what == '2':
        for j in range(N):
            if word[j][odr] == -1:
                word[j][odr] = 1
                word[j][26] -= 1
                if word[j][26] == 0:
                    remember += 1
    print(remember)
