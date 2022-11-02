n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(len(l)):
    s=s+l[i]
j=s/len(l)
print("{:.2f}".format(j))