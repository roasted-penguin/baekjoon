data = map(int,input().split())
numbers = list(data)
squared = []
S = 0

for i in range(len(numbers)):
  square = numbers[i]**2
  squared.append(square)
  S += square

R = S%10
print(R)
