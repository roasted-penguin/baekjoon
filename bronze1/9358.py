import math

T = int(input())
for i in range(T):
  N = int(input())
  seq = list(map(int,input().split()))
  while N > 2:
    paste = []
    length = len(seq)
    for j in range(math.ceil(length/2)):
      paste.append(seq[j] + seq[length-1-j])
    seq = paste
    N /= 2
  if seq[0] > seq[1]:
    print("Case #"+str(i+1)+": Alice")
  else:
    print("Case #"+str(i+1)+": Bob")
