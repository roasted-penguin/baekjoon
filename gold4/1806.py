import sys
N, S = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

start, end = 0, 0
sum = arr[start]
# 시작 수부터 S 넘으면 더 검사할필요 없이 가장짧은 길이인 1 출력
if sum >= S:
  print(1)
else:
  cnt = 10**9
  # start,end가 모두 끝까지 가거나, 길이 1일때 S 넘으면 break
  while True:
    if end == N-1:
      if start == end:
        break
      sum -= arr[start]
      start += 1
    elif start == end:
      if end == N-1 or sum >= S:
        break
      end += 1
      sum += arr[end]
      
    else:
      if sum > S:
        sum -= arr[start]
        start += 1
      else:
        end += 1
        sum += arr[end]
    if sum >= S:
      cnt = min(cnt,end-start+1)

  if cnt == 10**9:
    print(0)
  else:
    print(cnt)
