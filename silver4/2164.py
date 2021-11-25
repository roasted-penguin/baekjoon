"""

# 1. pop은 O(n)소요 -> while문 O(n^2) -> 시간초과(50만^2)

N = int(input())

card = []
for i in range(N):
  card.append(i+1)
length = len(card)


while(length!=1):
  card.pop(0) # pop은 O(n)소요 -> while문 O(n^2)
  switch = card.pop(0)
  card.append(switch)
  length -= 1
  # print(card)
  # print(length)

print(card[0])
"""

#deque으로 코드짜기

from collections import deque

N = int(input())

card = deque()
for i in range(N):
  card.append(i+1)
length = len(card)

while(length!=1):
  card.popleft()
  switch = card.popleft()
  card.append(switch)
  length -= 1
  # print(card)
  # print(length)

print(card[0])
