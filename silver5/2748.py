N = int(input())

fibonacci = [0,1]
for i in range(2,N+1):
  fib = fibonacci[i-2] + fibonacci[i-1]
  fibonacci.append(fib)
print(fibonacci[N])
