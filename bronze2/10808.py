sen = input()
alphabet = [0 for i in range(26)]
for i in range(len(sen)):
  alphabet[ord(sen[i]) - 97] += 1

for i in range(26):
  print(alphabet[i],end=" ")
