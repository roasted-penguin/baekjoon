koong = [1,1,2,4]
for i in range(4,68):
    koong.append(koong[i-1]+koong[i-2]+koong[i-3]+koong[i-4])

t = int(input())
for _ in range(t):
    n = int(input())
    print(koong[n])
