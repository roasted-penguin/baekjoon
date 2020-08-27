n = int(input())
stack = []
ans = []
toput = 1
bln = True

for i in range(n):
  num = int(input())
  while toput <= num:
    stack.append(toput)
    ans.append("+")
    toput += 1
  if stack[-1] == num:
    stack.pop()
    ans.append("-")
  else:
    bln = False
    break

if bln:
  for i in range(len(ans)):
    print(ans[i])
else:
  print("NO")
