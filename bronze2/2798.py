N, M = map(int,input().split())
card = list(map(int,input().split()))
maxsum = 0
for i in range(0,N):
  for j in range(i+1,N):
    for k in range(j+1,N):
      S = card[i] + card[j] + card[k]
      if S > maxsum and S <= M:
        maxsum = S
print(maxsum)
