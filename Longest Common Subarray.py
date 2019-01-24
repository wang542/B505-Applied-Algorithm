#chenxu wang
#wang542
#PA3


#a,b arrays
#m,n length of arrays
def lcs(a,b,m,n):
    #Initialize array
    lmatrix=[[0 for i in range(n+1)] for i in range(m+1)]

    #Build array
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                lmatrix[i][j]=0
            elif a[i-1]==b[j-1]:
                lmatrix[i][j]=lmatrix[i-1][j-1]+1
            else:
                lmatrix[i][j]=max (lmatrix[i-1][j],lmatrix[i][j-1])

    #retrieve element 
    result=""
    x=len(a)
    y=len(b)

    while x!=0 and y!=0:
        if lmatrix[x][y]==lmatrix[x-1][y]:
            x-=1
        elif lmatrix[x][y]==lmatrix[x][y-1]:
            y-=1
        else:
            result=str(a[x-1])+result
            x-=1
            y-=1
    return result
    


#test
x=["a","b","c","b","d","a","b"]
y=["b","d","c","a","b","a"]


q=[1,0,0,1,0,1,0,1]
w=[0,1,0,1,1,0,1,1,0]

print(lcs(x,y,len(x),len(y)))
print(lcs(q,w,len(q),len(w)))
