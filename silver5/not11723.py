#시간초과
N = int(input())
S = []
for _ in range(N):
    sen = input().split()
    if sen[0] != "all" and sen[0] != "empty":
        num = int(sen[1])
    
    if sen[0] == "add":
        S.append(num)
    elif sen[0] == "remove":
        for i in range(len(S)):
            if S[i] == num:
                S.remove(num)
    elif sen[0] == "check":
        boolean = 1
        for i in range(len(S)):
            if S[i] == num:
                boolean = 0
                print(1)
                break
        if boolean:
            print(0)
    elif sen[0] == "toggle":
        boolean = 1
        for i in range(len(S)):
            if S[i] == num:
                boolean = 0
                S.remove(num)
                break
        if boolean:
            S.append(num)
    elif sen[0] == "all":
        S = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    elif sen[0] == "empty":
        S = []
    S = list(set(S))
