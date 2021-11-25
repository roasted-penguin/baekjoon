T = int(input())
for i in range(T):
  N = int(input())

  if N == 0:
    print(1,0)
  elif N == 1:
    print(0,1)
  else:
    fn_1 = 1
    fn_2 = 0
    loop = 2
    while N >= loop:
      fn = fn_1 + fn_2
      fn_2 = fn_1
      fn_1 = fn
      loop += 1
    print(fn_2,fn_1)
