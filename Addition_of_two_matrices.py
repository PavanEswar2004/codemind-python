r=int(input())
m1=[]
m2=[]
m3=[]
for i in range(r):
    m1.append(list(map(int,input().split())))
for i in range(r):
    m2.append(list(map(int,input().split())))
for i in range(r):
    l=[]
    for j in range(r):
        l.append(m1[i][j]+m2[i][j])
    m3.append(l)
for i in range(r):
    for j in range(r):
        print(m3[i][j],end=" ")
    print()