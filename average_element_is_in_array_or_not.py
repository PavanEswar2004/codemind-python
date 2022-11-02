n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(len(l)):
    s=s+i
av=s/len(l)
for j in range(len(l)):
    if av in l:
        print("True")
        break
else:
    print("False")