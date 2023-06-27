r,c=map(int,input().split())
mat=[]
for i in range(r):
    innerlist=list(map(int,input().split()))
    mat.append(innerlist)
x=[]
y=[]
for i in range(r):
    for j in range(c):
        if mat[i][j]%2==0:
            x.append(mat[i][j])
        else:
            y.append(mat[i][j])
s=sum(x)
s2=sum(y)
print(s,s2)