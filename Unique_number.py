n=int(input())
n=str(n)
x=[]
c=0
for i in n:
    if i not in x:
        x.append(i)
    else:
        c=c+1
if c>0:
    print("Not Unique Number")
else:
    print("Unique Number")