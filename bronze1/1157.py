"""
1. 아스키코드 A~Z=65~90 소문자 = 대문자 +32
2. 문자 = chr(아스키)
3. 아스키코드 = ord(문자)

Dumb
1. sentence[j] == chr(i) or chr(i+32) -> sentence[j] == chr(i) or sentence[j] == chr(i+32)
2. 시간초과와의 싸움 [input size 10^6인데 O(n^2)코드짬]
#중요
Major(1).len()은 문자열 길이만큼 돌아가면서 길이를 구하므로  n번 도는 for문 안에 껴있으면 *n해주는것과 마찬가지이다.
Minor(1).input()보다 import sys/sys.stdin.readline()이 빠르다
Minor(2). 두번째 loop안에는 최대한 시간초과 요소를 집어넣지 않는다 ex)or와 같은 비교연산자, j loop 인데 chr(i)와 같은 불필요한 반복함수호출

코드
sentence = input()
most = 0
aum = 0 #alphabet used most
# print(chr(65))
# print(len(sentence))
for i in range(65,91):
  count = 0
  for j in range(len(sentence)):
    if sentence[j] == chr(i) or sentence[j] == chr(i+32):
      count += 1
  if count > most:
    most = count
    aum = i
  elif count == most:
    aum = 0 #to print "?"
  # print(count, most, aum)

if aum != 0:
  print(chr(aum))
else:
  print("?")
"""
import sys

sentence = sys.stdin.readline()
sentence = sentence.upper()# change into capital
length = len(sentence)
most = 0
aum = 0 #alphabet used most
for i in range(65,91):
  count = 0
  alphabet = chr(i)
  for j in range(length):
    if sentence[j] == alphabet:
      count += 1
  if count > most:
    most = count
    aum = i
  elif count == most:
    aum = 0 #to print "?"

if aum != 0:
  print(chr(aum))
else:
  print("?")
