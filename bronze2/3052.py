thelist = [0 for i in range(42)]
count = 0

for i in range(10):
  number = int(input())
  thelist[number%42] += 1

for j in range(42):
  if thelist[j] != 0:
    count += 1

print(count)
