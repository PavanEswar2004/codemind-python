t=int(input())
for i in range(t):
    x=int(input())
    l=list(map(int,input().split()))
    if l==sorted(l):
        print(0)
    else:
        print(max(l)-min(l))