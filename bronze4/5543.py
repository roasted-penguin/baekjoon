burger = []
beverage = []
for i in range(5):
    num = int(input())
    if i <= 2:
        burger.append(num)
    else:
        beverage.append(num)

ans = 1e9
for i in range(3):
    for j in range(2):
        ans = min(ans, burger[i] + beverage[j])

print(ans-50)
