N = int(input())
bill = []

for i in range(N):
  call = int(input())
  if call!=0:
    bill.append(call)
  else:
    bill.pop()
print(sum(bill))
