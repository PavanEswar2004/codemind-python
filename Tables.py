m,n=map(int,input().split())
for i in range(1,n+1):
    if (i%2!=0):
        k=m*i
        print(f"{m} x {i} = {k}")
