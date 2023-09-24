import sys
N = int(sys.stdin.readline())
arr = [list(map(str,sys.stdin.readline().rstrip())) for _ in range(N)]

num_dict = dict()
for i in range(N):
  item = arr[i]
  S = 1
  # 문자가 몇자리수에 몇번 나오는지 count하여 문자를 key로가지는 dictionary에 저장
  while len(item) > 0:
    new = item.pop()
    if new in num_dict:
      num_dict[new] = num_dict[new] + S
    else:
      num_dict[new] = S
    S *= 10
# dictionary를 value를 기준으로 내림차순으로 정렬
new_dict = dict(sorted(num_dict.items(),key=lambda x:x[1], reverse=True))
num_arr = list()
for item in new_dict:
  num_arr.append(new_dict[item])

# 가중치 곱해서 계산
res = 0
weight = 9
for value in num_arr:
  res += (value * weight)
  weight -= 1
print(res)
