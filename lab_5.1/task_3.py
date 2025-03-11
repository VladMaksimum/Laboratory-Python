f = open("lab_5/kidgar.txt")
ol = open("lab_5/oldest.txt", 'w')
yn = open("lab_5/youngest.txt", 'w')

kids = []
for i in f:
    kids.append(i.split())

ma=0
mi=100000000
for i in range(len(kids)):
    if ma<int(kids[i][2]):
        ma=int(kids[i][2])
        resma=i
    if mi>int(kids[i][2]):
        mi=int(kids[i][2])
        resmi=i

ol.write(' '.join(kids[resma]))
yn.write(' '.join(kids[resmi]))

f.close()
ol.close()
yn.close()