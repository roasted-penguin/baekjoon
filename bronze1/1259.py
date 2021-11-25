while True:
  data = input()
  if data == '0':
    break

  length = len(data)
  if length%2 != 0:
    loop = length//2 + 1
  else:
    loop = length//2
  
  state = True
  for i in range(loop):
    if data[i] != data[length-i-1]:
      state = False
      break
  if state == True:
    print('yes')
  else:
    print('no')
