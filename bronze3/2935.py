A = input()
sign = input()
B = input()
if sign == "*":
  length = len(A)+len(B)-1
  ans = "1"
  for i in range(length-1):
    ans += "0"
else:
  if len(A)==len(B):
    ans = "2"
    length = len(A)
    for i in range(length-1):
      ans += "0"
  else:
    length = max(len(A),len(B))
    put = min(len(A),len(B))
    ans = "1"
    for i in range(length-1):
      if i != length-put-1:
        ans += "0"
      else:
        ans += "1"
print(ans)
