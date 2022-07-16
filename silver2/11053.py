N = int(input())
A = list(map(int,input().split()))
S = []
ans = 1
for i in range(len(A)):
    max = 1
    for j in range(len(S)):
        if A[i] > A[j]:
            if max <= S[j]:
                max = S[j]+1
    if ans <= max:
        ans = max
    S.append(max)
print(ans)
