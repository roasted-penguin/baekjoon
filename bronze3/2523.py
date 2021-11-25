N = int(input())
arr = []

for i in range(N-1):
  sen = ""
  for j in range(i+1):
    sen += "*"
  arr.append(sen)
  
sen = ""
for i in range(N):
  sen += "*"
arr.append(sen)

for i in range(N-1):
  sen = ""
  for j in range(N-i-1):
    sen += "*"
  arr.append(sen)

for i in range(len(arr)):
  print(arr[i])
