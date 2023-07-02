n=int(input())
for i in range(n):
    k=input()
    if k==(k[::-1]) and (len(k)%2==0):
        print("YES EVEN")
    elif k==(k[::-1]) and (len(k)%2!=0):
        print("YES ODD")
    else:
        print("NO")