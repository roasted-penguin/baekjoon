sen = input()
cnt = 0
length = len(sen)
while sen:
  if sen[0] in ["c","s","z"]:
    if sen[0] == "c":
      if length >= 2 and sen[1] in ["=","-"]:
        sen = sen[2:]
        length -= 2
      else:
        sen = sen[1:]
        length -= 1
    else:
      if length >= 2 and sen[1] == "=":
        sen = sen[2:]
        length -= 2
      else:
        sen = sen[1:]
        length -= 1
  elif sen[0] == "d":
    if length >= 2 and sen[1] == "-":
      sen = sen[2:]
      length -= 2
    elif length >= 2 and sen[1] == "z":
      if length >= 3 and sen[2] == "=":
        sen = sen[3:]
        length -= 3
      else:
        sen = sen[1:]
        length -= 1
    else:
      sen = sen[1:]
      length -= 1
  elif sen[0] in ["l","n"]:
    if length >= 2 and sen[1] == "j":
      sen = sen[2:]
      length -= 2
    else:
      sen = sen[1:]
      length -= 1
  else:
    sen = sen[1:]
    length -= 1
  cnt += 1
print(cnt)
