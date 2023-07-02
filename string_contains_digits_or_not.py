n=int(input())
for i in range(n):
    k=input()
    c=0
    for i in k:
        if i not in "1234567890":
            continue
        else:
            c=c+1
    if c!=0:
        print("Yes")
    else:
        print("No")