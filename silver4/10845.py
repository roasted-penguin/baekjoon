import sys

N = int(input())
queue = []
for i in range(N):
  query = list(sys.stdin.readline().split())
  if query[0] == 'push':
    queue.append(int(query[1]))
  if query[0] == 'pop':
    if len(queue) != 0:
      print(queue.pop(0))
    else:
      print(-1)
  if query[0] == 'size':
    print(len(queue))
  if query[0] == 'empty':
    if len(queue) != 0:
      print(0)
    else:
      print(1)
  if query[0] == 'front':
    if len(queue) != 0:
      print(int(queue[0]))
    else:
      print(-1)
  if query[0] == 'back':
    if len(queue) != 0:
      print(int(queue[-1]))
    else:
      print(-1)
