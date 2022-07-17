N = input()
arr = [0 for _ in range(10)]
for i in range(len(N)):
    n = int(N[i])
    arr[n] += 1

sen = ""
for i in range(10):
    n = 9-i
    if arr[n] != 0:
        sen += str(n)*arr[n]

print(sen)
