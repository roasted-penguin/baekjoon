# 결국은 피보나치 수열문제

N = int(input())
fibonacci = [1,2]
fib = 2
while True:
  fib = fibonacci[-1] + fibonacci[-2]
  if fib > N:
    break
  fibonacci.append(fib)

# print("fibonacci sequence is...",fibonacci)
cnt = 0
while N > 0:
  num = fibonacci.pop()
  cnt += 1
  if N == num:
    ans = num
    break
  elif  N > num:
    N -= num
    # print(num+N, "=",num,"+",N)
if cnt == 1:
  print(-1)
else:
  print(ans)
