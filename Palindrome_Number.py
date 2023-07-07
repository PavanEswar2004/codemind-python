def pal(num):
    k=num
    s=0
    while num:
        r=num%10
        s=s*10+r
        num=num//10
    if s==k:
        return True
    else :
        return False

n=int(input())
for i in range(n):
    t=int(input())
    if t<0:
        print("False")
    else:
        print(pal(t))