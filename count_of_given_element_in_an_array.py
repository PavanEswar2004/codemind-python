n=int(input())
l=list(map(int,input().split()))
k=int(input())
cn=0
for i in l:
    if k==i:
        cn=cn+1
print(cn)
    