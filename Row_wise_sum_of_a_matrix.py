r,c=map(int,input().split())
m=[]
for i in range(r):
    innerlist=list(map(int,input().split()))
    m.append(innerlist)

x=[]
for i in range(r):
    y=sum(m[i])
    x.append(y)
print(*x)