N = int(input())
R, G, B = 0, 0 ,0
for i in range(N):
    r, g, b = map(int,input().split())
    R_ ,G_ ,B_ = R, G, B
    R = min(G_+r,B_+r)
    G = min(R_+g,B_+g)
    B = min(G_+b,R_+b)
print(min(R,G,B))
