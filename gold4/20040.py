n, m = map(int,input().split())
parent = [i for i in range(n)]

def find(a):
    if parent[a] != a:
        return find(parent[a])
    else:
        return a

def union(a,b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
        return True
    elif b > a:
        parent[b] = a
        return True
    else:
        return False

answer = 0
for i in range(m):
    x, y = map(int,input().split())
    if not union(x,y):
        answer = i + 1
        break

print(answer)
