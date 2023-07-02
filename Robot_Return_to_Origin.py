n=input()
x=0
y=0
for i in n:
    if i =="U":
        y=y+1
    elif i=="D":
        y=y-1
    elif i == "L":
        x=x+1
    elif i=="R":
        x=x-1
if x==0 and y==0:
    print("True")
else:
    print("False")
        