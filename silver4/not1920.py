# 런타임 
N = int(input())
A = list(map(int,input().split()))
A = sorted(A)
Alen = len(A)

M = int(input())
numbers = list(map(int,input().split()))

def Binsearch(arr,find,low,high):
    if low > high:
        return False
    else:
        mid = (low+high)//2
    
        if arr[mid]==find:
            return True
        else:
            if arr[mid] > find:
                return Binsearch(arr,find,low,mid-1)
            else:
                return Binsearch(arr,find,mid+1,high)

for i in range(M):
    num = numbers[i]
    if Binsearch(A,num,0,Alen):
        print(1)
    else:
        print(0)
