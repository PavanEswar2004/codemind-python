r, c = map(int, input().split())
m = []
for i in range(r):
    il = list(map(int, input().split()))
    m.append(il)
x=[]
for i in range(1,r-1):
    for j in range(1,c-1):
        x.append(m[i][j])
print(sum(x))