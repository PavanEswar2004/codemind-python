n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if i%2!=0:
        c=c+1
if c>=3:
    print("NO")
else:
    print("YES")