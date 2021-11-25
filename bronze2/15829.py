L = int(input())
sentence = str(input())
H = 0
for i in range(L):
  num = ord(sentence[i])-96
  H += num*31**i
  H %= 1234567891
print(H)
