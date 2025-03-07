def count_digits(str):
    dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    for i in str:
        dict[int(i)] +=1
    
    res = {}
    for j in range(3):
        m = 0
        mn=0
        for n in dict:
            if m<dict[n]:
                mn=n
                m=dict[n]
        res[mn] = m
        del dict[mn]
    
    return res

print(count_digits("100134729365"))