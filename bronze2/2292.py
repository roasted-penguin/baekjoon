"""
1 1 1개
2-7 2 6개
8-19 3 12개
20-37 4 18개

일반화
1+6+...+6(n-2)+1~1+6+...6(n-1)
n 6(n-1)개

"""
N = int(input())
arr = [0,1]
i = 2
num = 0
while num < 1000000000:
  num = 3*i**2 - 9*i + 8
  arr.append(num)
  i += 1

for i in range(len(arr)):
  if arr[i+1] > N:
    print(i)
    break
