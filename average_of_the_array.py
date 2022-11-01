n=int(input())
s=0
l=list(map(int,input().split()))
for i in range(len(l)):
    s=s+l[i]
k=s/len(l)
print("{:.2f}".format(k))