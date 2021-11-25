T = int(input())
matrix = [[[6,-4],[1,0]]]
def multmatrix(x,y):
    a = (x[0][0]*y[0][0]+x[0][1]*y[1][0])%1000
    b = (x[0][0]*y[0][1]+x[0][1]*y[1][1])%1000
    c = (x[1][0]*y[0][0]+x[1][1]*y[1][0])%1000
    d = (x[1][0]*y[0][1]+x[1][1]*y[1][1])%1000
    toreturn = [[a,b],[c,d]]
    

    return toreturn

for i in range(50):
    mat = matrix[i]
    matrix.append(multmatrix(mat,mat))


for i in range(T):
    n = int(input())
    if n == 1:
        ans = 6
    elif n == 2:
        ans = 28
    else:
        bin = format(n-2,'b')
        ansmat = [[1,0],[0,1]]
        for j in range(len(bin)):
            if bin[-1] == '1':
                ansmat = multmatrix(matrix[j],ansmat)
            bin = bin[:-1]
        ans = ansmat[0][0]*28+ansmat[0][1]*6

    ans = (ans+999)%1000
    ans = str(ans)
    while len(ans)<3:
        ans = "0" + ans

    print("Case #{a}: {b}".format(a=i+1,b=ans))


'''
6 -4 28
1 0  6
'''
