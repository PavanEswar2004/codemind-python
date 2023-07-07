n=int(input())
x=[0,1]
a=0
b=1
count=0
while count<=n:
    c=a+b
    x.append(c)
    count=count+1
    a=b
    b=c
    c=a+b
oc=0
for i in range(0,n):
    print(x[i],end=" ")
    