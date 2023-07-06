n = int(input())
strnum = str(n)
maxnum = n
for i in range(len(strnum)):
    if strnum[i] == '6':
        newnum = int(strnum[:i] + '9' + strnum[i+1:])
        maxnum = max(maxnum, newnum)
    elif strnum[i] == '9':
        newnum = int(strnum[:i] + '6' + strnum[i+1:])
        maxnum = max(maxnum, newnum)
print(maxnum)
