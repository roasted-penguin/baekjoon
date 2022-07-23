import sys
S = [False for _ in range(21)]
F = [False for _ in range(21)]
T = [True for _ in range(21)]
M = int(input())
for i in range(M):
    func = list(map(str,sys.stdin.readline().split()))
    print("func is ",func)
    #add remove check toggle all empty
    num = 0
    if len(func)==2:
        num = int(func[1])
    if func[0] == "add":
        S[num] = True
    elif func[0] == "remove":
        S[num] = False
    elif func[0] == "check":
        if S[num]:
            print(1)
        else:
            print(0)
    elif func[0] == "toggle":
        S[num] = not S[num]
    elif func[0] == "all":
        S = T
    elif func[0] == "empty":
        S = F
