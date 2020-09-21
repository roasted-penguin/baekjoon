for i in range(3):
  yoot = list(map(int,input().split()))
  cnt = 0
  for j in range(4):
    if yoot[j] == 0:
      cnt += 1
  ans = ["E","A","B","C","D"]
  for j in range(5):
    if cnt == j:
      print(ans[j])
