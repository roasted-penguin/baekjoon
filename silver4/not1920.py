N = int(input())

A = list(map(int,input().split()))
A = sorted(A)
length_A = len(A)

M = int(input())
X = list(map(int,input().split()))

def binsearch(front,end,arr,number):
  if number > end:


for i in range(M):
  if binsearch(0,length_A,A,X[i]):
    print(1)
  else:
    print(0)


number = 3
1 2 3 4 4 5 6 6
if number == arr[length//2]:
  return True
elif number > arr[length//2]:
  return binsearch(arr,number)
else:
  return binsearch()
1 2 3 4 4 5 6 6 7 arr[length//2]
