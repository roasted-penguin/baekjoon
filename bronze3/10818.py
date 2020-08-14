N = int(input())
number = []
number = input().split()

max = int(number[0])
min = int(number[0])

for i in range(N):
  if int(number[i]) > max:
    max = int(number[i])
  elif int(number[i]) < min:
    min = int(number[i])

print(min,max)
