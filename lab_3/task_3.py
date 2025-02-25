#exp = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']
exp = ['aaa', 'bbb', 'ccc']
#exp = ['abc', 'abc', 'abc']
dict = {}
uniq = []

for k in exp:
    if k not in uniq:
        uniq.append(k)

for i in exp:
    if i in dict:
        dict[i]+=1
    else:
        dict[i] = 1

for j in uniq:
    print(dict[j], end=" ")
print()

