s=input()
x=[]
for i in s:
    if i not in "1234567890":
        continue
    else:
        x.append(int(i))
print(sum(x))