N = int(input())
tile = [list(map(int,input().split())) for _ in range(N)]

direction = [[[0,0,0] for _ in range(N)] for _ in range(N)]

if tile[0][2] == 0:
    direction[0][2] = [1,0,0]
if [tile[0][2], tile[1][1], tile[1][2]] == [0,0,0]:
    direction[1][2] = [0,1,0]

for i in range(N):
    for j in range(N):
        print(i,j)
        if direction[i][j][0] > 0:#horizontal
            num = direction[i][j][0]
            if j+1 < N and tile[i][j+1] == 0:#move horizontal
                direction[i][j+1][0] += num
                print("h,h")
            if i+1 < N and j+1 < N  and tile[i][j+1] == 0 and tile[i+1][j+1]==0 and tile[i+1][j]==0:#move diagonal
                direction[i+1][j+1][1] += num
                print("h,d")
        if direction[i][j][1] > 0:#diagonal
            num = direction[i][j][1]
            if j+1 < N and tile[i][j+1] == 0:#move horizontal
                direction[i][j+1][0] += num
                print("d,h")
            if i+1 < N and j+1 < N  and tile[i][j+1]==0 and tile[i+1][j+1]==0 and tile[i+1][j]==0:#move diagonal
                direction[i+1][j+1][1] += num
                print("d,d")
            if i+1 < N and tile[i+1][j]==0:#move vertical
                direction[i+1][j][2] += num
                print("d,v")
        if direction[i][j][2] > 0:#vertical
            num = direction[i][j][2]
            if i+1 < N and j+1 < N  and tile[i][j+1]==0 and tile[i+1][j+1]==0 and tile[i+1][j]==0:#move diagonal
                direction[i+1][j+1][0] += num
                print("v,d")
            if i+1 < N and tile[i+1][j]==0:#move:#move vertical
                direction[i+1][j][2] += num
                print("v,v")

ans = direction[N-1][N-1][0] + direction[N-1][N-1][1] + direction[N-1][N-1][2]
print(ans)
print(direction)
