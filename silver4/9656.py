def benefitial(a,b,c):
  if b!=a:
    if c==a: return c
    else: return not a
  else: return b

def game(x,y):
  if x==1:
    return y
  elif x==2:
    return not y
  elif x==3:
    return y
  else: 
    return benefitial(y,game(x-1,not y),game(x-3,not y))

data = input()
if game(data,True)==True:
  print('SK')
else:
  print('CY')
