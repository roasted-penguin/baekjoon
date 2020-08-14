N = int(input())
max = -1000000
min = 1000000
number = []
number = input().split()

for i in range(N):
  if int(number[i]) > max:
    max = int(number[i])
  elif int(number[i]) < min:
    min = int(number[i])

print(min,max)
