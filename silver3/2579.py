n = int(input())
stair = []
for i in range(n):
    s = int(input())
    stair.append(s)
    
#초기값    
arr = [[0,0]]
arr.append([stair[0],0])
length = len(stair)
if length > 1:
    arr.append([stair[1],stair[0]+stair[1]])
#for문(n>=3)    
if length > 2:
    for i in range(3,length+1):
        v1 = max(arr[i-2][0],arr[i-2][1])+stair[i-1]
        v2 = arr[i-1][0]+stair[i-1]
        arr.append([v1,v2])
        
ans = max(arr[n][0],arr[n][1])
print(ans)
