num = input()
num = int(num)

for i in range(0,num):
  ans = ""
  repeat, sentence = input().split()
  repeat = int(repeat)
  for j in range(0,len(sentence)):
    for rep in range(repeat):
      ans += sentence[j]
  print(ans)
