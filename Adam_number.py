n=int(input())
sn=n*n
n=str(n)
rn=n[::-1]
rn=int(rn)
sn2=rn*rn
sn2=str(sn2)
sn2=int(sn2[::-1])
if sn==sn2:
    print("True")
else:
    print("False")