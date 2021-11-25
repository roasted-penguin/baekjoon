N = int(input())
words = []
for i in range(N):
  words.append(input())

words = list(set(words))

arranged = []

for wordlen in range(1,51):
  smalllist = []
  length = len(words)
  for i in range(length):
    if len(words[i]) == wordlen:
      smalllist.append(words[i])
  smalllist = sorted(smalllist)
  arranged.extend(smalllist)

lenarranged = len(arranged)
for i in range(lenarranged):
  print(arranged[i])
