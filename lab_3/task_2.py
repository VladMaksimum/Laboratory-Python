l1 = [int(i) for i in input("list 1 = ").split()]
l2 = [int(i) for i in input("list 2 = ").split()]

cnt=0
for i in l1:
    if i in l2:
        cnt+=1
print(cnt)

