T = int(input())
for _ in range(T):
    n = int(input())
    arr = []
    nums = []
    for i in range(n):
        name, type = map(str,input().split())
        if type not in arr:
            nums.append(1)
            arr.append(type)
        else:
            i = arr.index(type)
            nums[i] += 1
    # (a+1)(b+1)(c+1)...-1\
    # +1해주는 이유 : 안입는 경우 포함. -1해주는 이유 : 다 안입을때 제외
    res = 1
    for i in range(len(nums)):
        res *= (nums[i]+1)
    res -= 1
    print(res)
