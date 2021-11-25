N = int(input())

for i in range(N):
  sentence = input()
  length = len(sentence)
  stack = []
  for j in range(length):
    letter = sentence[j]
    state = True
    if letter == '(':
      stack.append(letter)

    if letter == ')':
      if not stack: # 빈 list는 false값 가진다
        print('NO')
        state = False
        break
      else:
        stack.pop()
  if state == True:
    if not stack:
      print('YES')
    else:
      print('NO')
