P = [1,1,1,2,2]
for i in range(5,100):
  Pi = P[i-1] + P[i-5]
  P.append(Pi)
  


T = int(input())
for i in range(T):
  N = int(input())
  print(P[N-1])
