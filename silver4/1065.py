arr = []
for i in range(1,100):
    arr.append(i)
start = [111,210,321,420,531,630,741,840,951]
for i in range(9):
    s = start[i]
    for j in range(5):
        arr.append(s + j*12)

        
N = int(input())
x = 0
l = len(arr)
while l > x and N >= arr[x]:
    x += 1
print(x)
