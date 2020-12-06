#플로이드 워셜 O(N^3)
INF = int(1e9)

N, M = map(int,input().split())

graph = [[INF for _ in range(N+1)] for _ in range(N+1)]
for i in range(1,N+1):
    graph[i][i] = 0
#print(graph)   
for i in range(M):
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

#플로이드 워셜!! for N : D(ab) = min(D(ab),D(ak)+D(kb))
for k in range(1,N+1):
    for a in range(1,N+1):
        for b in range(1,N+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])
            
KB = [0 for _ in range(N+1)] #Kevin Bacon
KB[0] = INF
for i in range(1,N+1):
    num = 0
    for j in range(1,N+1):
        if i != j:
            num += graph[i][j]
    KB[i] = num

print(KB.index(min(KB))) # 최솟값 인덱스 호출
