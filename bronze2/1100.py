chess = []
ans = 0
for i in range(8):
  chess.append(input())

for i in range(8):
  for j in range(8):
    if (i+j) % 2 == 0:
      if chess[i][j] == "F":
        ans += 1

print(ans)
