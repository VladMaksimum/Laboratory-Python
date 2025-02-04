string = input()
lets = list(set(string))

res=[]
for i in range(len(lets)):
    cnt=0
    for j in range(len(string)):
        if string[j] == lets[i]:
            cnt+=1
    res.append([cnt,lets[i]])

res = sorted(res)[::-1]
for i in range(3):
    print(res[i][1], res[i][0])