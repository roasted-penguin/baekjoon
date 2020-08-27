"""
아파트구조
2층 1 4 10 20 35 56
1층 1 3 6 10 15 21
0층 1 2 3 4 5 6
"""
T = int(input())
apartment = []
floor0 = []
for i in range(1,15):
  floor0.append(i)
apartment.append(floor0)

for i in range(1,15):
  floori = [1]
  for j in range(1,14):
    floori.append(floori[j-1] + apartment[-1][j])
  apartment.append(floori)

for i in range(T):
  k = int(input())
  n = int(input())
  print(apartment[k][n-1])
