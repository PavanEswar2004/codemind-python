n=int(input())
x=[]
a=0
b=1
c=0
while c<=n:
    c=a+b
    x.append(c)
    a=b
    b=c
    c=a+b
if n in x:
    print("True")
else:
    print("False")