N = int(input())
weights = list(map(int,input().split()))
M = int(input())
beads = list(map(int,input().split()))

plus = [0]
for i in range(len(weights)):
    w = weights[i]
    pluss = plus
    for j in range(len(plus)):
        pluss.append(plus[j]+w)
    plus = list(set(pluss))
    # print(plus)
"""
minus = [0]
l = len(weights)
for i in range(len(weights)):
    w = weights[l-i-1]
    minuss = minus
    minuss.append(w)
    for j in range(len(minus)):
        if minus[j]-w > 0:
            minuss.append(minus[j]-w)
    minus = list(set(minuss))
    print(minus)

for i in range(M):
    if beads[i] in plus or beads[i] in minus:
        print("Y",end=" ")
    else:
        print("N",end=" ")
"""
copy = plus
for i in range(len(plus)):
    pluss = plus
    w = copy[i]
    for j in range(len(copy)):
        pluss.append(abs(copy[j]-w))
    plus = list(set(pluss))
    # print(plus)    
        
for i in range(M):
    if beads[i] in plus:
        print("Y",end=" ")
    else:
        print("N",end=" ")
