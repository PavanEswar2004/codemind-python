n=int(input())
x=[]
for i in range(1,n):
    if n%i==0:
        x.append(i)
if sum(x)>n:
    print("True")
else:
    print("False")