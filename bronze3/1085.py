x, y, w, h = map(int,input().split())
print(min([y,h-y,w-x,x]))
