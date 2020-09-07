import math
sentence = input()
ispalindrome = True
length = len(sentence)
for i in range(math.ceil(length/2)):
  if sentence[i] != sentence[length-i-1]:
    ispalindrome = False
    break
if ispalindrome:
  print(1)
else:
  print(0)
