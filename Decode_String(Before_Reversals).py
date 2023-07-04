t=int(input())
for i in range(t):
    l,r=map(int,input().split())
    x=input()
    while r>0:
        p=x[:r]
        p=p[::-1]
        x=p+x[r:]
        r=r-1
    print(x)


