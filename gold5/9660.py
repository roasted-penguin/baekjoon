"""
N<= 1조이므로 수열의 규칙으로 푼다
"""
N = int(input())
if N%7 == 2 or N%7 == 0:
  print('CY')
else:
  print('SK')
