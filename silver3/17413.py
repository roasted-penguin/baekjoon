S = input()
sen = ""
res = ""
lenS = len(S)
i = 0
flag = False


while i < lenS:
    c = S[i]
    if flag:
        res += c
        if c == ">":
            flag = False
    else:
        if c == "<":
            flag = True
            if sen != "":
                res = res + sen[::-1] + c
                sen = ""
            else:
                res += c
        elif c == " ":
            res = res + sen[::-1] + c
            sen = ""
        else:
            sen += c
    i += 1
  
res = res + sen[::-1] 
print(res)
