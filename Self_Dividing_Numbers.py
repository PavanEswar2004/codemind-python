def sd(n):
    k = n
    num = str(k)
    l = len(num)
    c = 0
    for i in num:
        if int(i)!=0 and k % int(i) == 0:
            c = c + 1
    if c == l:
        return True
    else:
        return False

n = int(input(""))
m = int(input(""))
x = []
for i in range(n, m + 1):
    if sd(i):
        x.append(i)

print(*x)
