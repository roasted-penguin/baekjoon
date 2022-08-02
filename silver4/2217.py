N = int(input())
rope = []
for _ in range(N):
    rope.append(int(input()))
rope.sort()

max = 0
k = N
for i in range(N):
    if max < rope[i]*k:
        max = rope[i]*k
    k -= 1

print(max)
