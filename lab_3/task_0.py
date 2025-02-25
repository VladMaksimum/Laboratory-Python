lst = [3,5,2,0,1]
res = []

for i in range(1,len(lst)):
    if lst[i] > lst[i-1]:
        res.append(lst[i])

print(res)

