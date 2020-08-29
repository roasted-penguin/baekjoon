while True:
  lengths = list(map(int,input().split()))
  lengths.sort()
  if lengths == [0, 0, 0]:
    break
  else:
    if lengths[2]**2 == lengths[0]**2 + lengths[1]**2:
      print("right")
    else:
      print("wrong")
