n=input()
c=0
for i in n:
    if i not in "1234567890":
        continue
    else:
        c=c+1
if c!=0:
    print(f"Contains {c} digit")
else:
    print("Doesn't contain digit")