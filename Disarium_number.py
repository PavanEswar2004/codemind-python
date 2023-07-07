n=int(input())
n=str(n)
l=list(n)
s=0
for i in range(0,len(n)):
    s=s+((int(l[i])**(i+1)))
if s==int(n):
    print("True")
else:
    print("False")
    