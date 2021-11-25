N = int(input())

for i in range(N):
  XOXO = input()

  success = 0
  score = 0

  for j in range(len(XOXO)):
    if XOXO[j] == 'O':
      success += 1
      score += success
    else:
      success = 0
  print(score)
