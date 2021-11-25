sen = input()
length = len(sen)
while True:
  if length > 10:
    print(sen[:10])
    sen = sen[10:]
    length -= 10
  else:
    print(sen)
    break
