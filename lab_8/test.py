from func_for_csv import Show


Show("lab_8/username.csv", type='r', lines=3)



'''
    for i in range(1,len(rfile)):
        tmp={}
        for j in range(len(rfile[i])):
            if j!=(len(rfile[i])-1):
                tmp[rfile[0][j]] = rfile[i][j]
            else:
                tmp[rfile[0][j][:-1:]] = rfile[i][j][:-1:]
        data.append(tmp)
'''
