alphabets = [-1 for i in range(26)]
sentence = input()

for i in range(len(sentence)):
  if alphabets[ord(sentence[i])-97] == -1:
    alphabets[ord(sentence[i])-97] = i

for j in range (26):
  print(alphabets[j], end = ' ')
