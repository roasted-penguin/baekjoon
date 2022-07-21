from collections import deque
T = int(input())
for _ in range(T):
    str = input()
    n = int(input())

    sen = input()
    if sen == "[]":
        q = deque()
    else:
        q = deque(map(int,sen[1:-1].split(",")))
    tf = False

    if str.count('D') > n:
         print("error")
    else:
        for i in range(len(str)):
            if str[i] == 'R':
                tf = not tf
            else:
                if tf:
                    q.pop()
                else:
                    q.popleft()
        if tf:
            q.reverse()


        if q:
            print("[",end="")
            print(q[0],end="")
            for i in range(1,len(q)):
                print(",",end="")
                print(q[i],end="")
            print("]")
        else:
            print("[]")
