# Let s = 2xy+x+y, (2x+1)(2y+1) = 2s+1
# x,y>0 integer so that (2x+1)(2y+1) is composite
# find the 2s+1 is prime that cannot exist
import sys
a_arr = [2,3,5,7,11]
alen = len(a_arr)

def mod_pow(a,b,m):
    a = a%m
    r = 1
    while b>0:
        if b&1:
          r = (r * a) % m
        b = b>>1
        a = (a * a) % m
    return r

def miller_rabin(n,a):
    q = n-1
    k = 0
    while q%2==0:
        q = q>>1
        k += 1
    x = mod_pow(a,q,n)
    if x==1:
        return 1

    cal = q;
    for j in range(k):
        x = mod_pow(a,cal,n)
        if x==n-1:
            return 1
        cal = cal<<1

    return 0

def isPrime(n):
  for i in range(alen):
    a = a_arr[i]
    if not(miller_rabin(n,a)): return 0
  return 1


# cnt = 0
# for num in range(2,100001):
#   if isPrime(num):
#     cnt += 1
#     #print(num,end=', ')
# print(cnt)

#341 561 645
N = int(sys.stdin.readline())
cnt = 0
s = 0
for i in range(N):
    s = int(sys.stdin.readline())
    num = 2*s+1
    if isPrime(num):
        cnt += 1
print(cnt)
