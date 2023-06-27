r,c=map(int,input().split())
mat=[]
for i in range(r):
    innerlist=list(map(int,input().split()))
    mat.append(innerlist)
    
x=[]
y=[]
for i in range(r):
    for j in range(c):
        if i%2==0:
            x.append(mat[i][j])
        if i%2!=0:
            y.append(mat[i][j])
s=sum(x)
s2=sum(y)
print(s,s2)