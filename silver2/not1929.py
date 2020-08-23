import math
M, N = map(int,input().split())

prime = [2]


for i in range(3,N+1,2):
    boolean = True
    length = len(prime)
    for j in range(length):
        if i%prime[j] == 0:
            boolean = False
            # print('break')
            break
        if math.sqrt(i) <= prime[j]:
            # print('leak')
            break
    if boolean:
        prime.append(i)
            
for i in range(M,N+1):
    if i in prime:
        print(i)


