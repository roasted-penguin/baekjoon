import sys
from collections import deque

N = int(input())
deq = deque()
for i in range(N):
  query = list(sys.stdin.readline().split())
  if query[0] == 'push_front':
    deq.appendleft(int(query[1]))
  if query[0] == 'push_back':
    deq.append(int(query[1]))
    
  if query[0] == 'pop_front':
    if len(deq) != 0:
      print(deq.popleft())
    else:
      print(-1)
  if query[0] == 'pop_back':
    if len(deq) != 0:
      print(deq.pop())
    else:
      print(-1)
  if query[0] == 'size':
    print(len(deq))
  if query[0] == 'empty':
    if len(deq) != 0:
      print(0)
    else:
      print(1)
  if query[0] == 'front':
    if len(deq) != 0:
      print(int(deq[0]))
    else:
      print(-1)
  if query[0] == 'back':
    if len(deq) != 0:
      print(int(deq[-1]))
    else:
      print(-1)
