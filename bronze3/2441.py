N = int(input())

for i in range(N):
  sen = ""
  for j in range(i):
    sen += " "
  for j in range(N-i):
    sen += "*"
  print(sen)
