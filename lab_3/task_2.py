l1 = [int(i) for i in input("list 1 = ").split()]
l2 = [int(i) for i in input("list 2 = ").split()]
res = []

for i in l1:
    if i in l2 and i not in res:
        res.append(i)
        
print(len(res))

