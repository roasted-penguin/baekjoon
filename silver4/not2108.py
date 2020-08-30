#2,3번 실패

N = int(input())
arr = [0 for i in range(8001)]
S = 0
for i in range(N):
    num = int(input())
    #1
    S += num
    #2,3,4
    arr[num+4000] += 1
arith = round(S/N)

median = 0
mid = N//2
cnt = 0
didmid = True

freq = 0
mode = 0

small = 4001
big = 4000
smallcnt = 0
for i in range(len(arr)):
    comp = arr[i]
    if arr[i] > 0:
        if cnt + comp >= mid and didmid:
            median = comp
            didmid = False
        if comp >= freq:
            freq = comp
            mode = i-4000
        if small == 4001:
            small = i-4000
        big = i-4000
        cnt += comp

rangee = big - small
        
        
    
print(arith)
print(median)
print(mode)
print(rangee)
