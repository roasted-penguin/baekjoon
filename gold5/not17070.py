N = int(input())
tile = [list(map(int,input().split())) for _ in range(N)]

direction = [[[0,0,0] for _ in range(N)] for _ in range(N)]

if tile[0][2] == 0:
    direction[0][2] = [1,0,0]
if [tile[0][2], tile[1][1], tile[1][2]] == [0,0,0]:
    direction[1][2] = [0,1,0]

for i in range(N):
    for j in range(N):
        if direction[i][j][0] == 1:#horizontal
            if j+1 < N and tile[i][j+1] == 0:#move horizontal
                direction[i][j+1][0] += 1
            if i+1 < N and j+1 < N  and tile[i][j+1] == 0 and tile[i+1][j+1] and tile[i+1][j]:#move diagonal
                direction[i+1][j+1][1] += 1
        if direction[i][j][1] == 1:#diagonal
            if j+1 < N and tile[i][j+1] == 0:#move horizontal
                direction[i][j+1][0] += 1
            if i+1 < N and j+1 < N  and tile[i][j+1] == 0 and tile[i+1][j+1] and tile[i+1][j]:#move diagonal
                direction[i+1][j+1][1] += 1
            if i+1 < N and tile[i+1][j] == 0:#move vertical
                direction[i+1][j][2] += 1
        if direction[i][j][2] == 1:#vertical
            if i+1 < N and j+1 < N  and tile[i][j+1] == 0 and tile[i+1][j+1] and tile[i+1][j]:#move diagonal
                direction[i+1][j+1][0] += 1
            if i+1 < N and tile[i+1][j] == 0:#move:#move vertical
                direction[i+1][j][2] += 1

ans = direction[N-1][N-1][0] + direction[N-1][N-1][1] + direction[N-1][N-1][2]
print(ans)
print(direction)
