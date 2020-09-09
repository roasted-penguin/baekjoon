ans = []
for i in range(2):
  scores = list(map(int,input().split()))
  S = 0
  for j in range(4):
    S += scores[j]
  ans.append(S)
print(max(ans[0],ans[1]))
