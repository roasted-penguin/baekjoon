"""
1. input EOF에러 try,except문
"""
while True:
  try:
    a, b = map(int,input().split())
    print(a+b)
  except EOFError:
    break
