N = int(input())
stack = []
for i in range(N):
  query = list(input().split())
  if query[0] == 'push':
    stack.append(int(query[1]))
  if query[0] == 'pop':
    if len(stack) != 0:
      print(stack.pop())
    else:
      print(-1)
  if query[0] == 'size':
    print(len(stack))
  if query[0] == 'empty':
    if len(stack) != 0:
      print(0)
    else:
      print(1)
  if query[0] == 'top':
    if len(stack) != 0:
      print(int(stack[-1]))
    else:
      print(-1)
