N = int(input())
game = list()
for i in range(N):
    g = list(map(int,input().split()))
    if i == 0:
        max1 = g
        min1 = g
    else:
        max0 = max1
        min0 = min1
        max1 = [max(max0[0],max0[1])+g[0],max(max0[0],max0[1],max0[2])+g[1],max(max0[1],max0[2])+g[2]]
        min1 = [min(min0[0],min0[1])+g[0],min(min0[0],min0[1],min0[2])+g[1],min(min0[1],min0[2])+g[2]]
        
print(max(max1),min(min1))
