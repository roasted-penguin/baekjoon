subject = int(input())
data = map(int,input().split())
scores = list(data)

length = len(scores)
M = max(scores)
S = 0

for i in range(length):
  scores[i] = scores[i]/M*100
  S += scores[i]
A = S/length
print(A)
