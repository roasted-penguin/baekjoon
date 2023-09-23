import sys
# 파이썬 입력 속도 에바
N ,M = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))
summed = [0]
acc = 0
for i in range(N):
  acc += nums[i]
  summed.append(acc)

for i in range(M):
  a, b = map(int,sys.stdin.readline().split())
  print(summed[b] - summed[a-1])
