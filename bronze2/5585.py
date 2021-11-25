money = int(input())
change = 1000 - money
coin = [500,100,50,10,5,1]

ans = 0
for i in range(len(coin)):
  c = coin[i]
  ans += change // c
  change %= c

print(ans)
