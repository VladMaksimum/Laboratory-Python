import random
from pathlib import Path


def Show(file_name, type='t', lines=5, separator=';'):
    with open(file_name) as file:
        data=[i.split(separator) for i in file.readlines()]
        for elm in data:
            if(len(elm)!=len(data[0])):
                elm.append('')
            elm[3] = elm[3][:-1:]

    for col in range(len(data[0])):
        maxlen=0
        for line in range(len(data)):
            maxlen = max(maxlen, len(data[line][col]))
        for i in range(len(data)):
            data[i][col] += ' ' * (maxlen-len(data[i][col]) + 1)
    
    if type=='t':
        if len(data)<=lines:
            for l in data:
                print(''.join(l))
                print("Not enough lines")
        else:
            for i in range(lines+1):
                print(''.join(data[i]))
    elif type=='b':
        print(''.join(data[0]))
        if len(data)-1<lines:
            for l in range(len(data)-1):
                print(''.join(data[::-1][l]))
            print("Not enough lines")
        else:
            for i in range(lines):
                print(''.join(data[len(data)-1-i]))
    elif type=='r':
        print(''.join(data[0]))
        tmp=data[1::]
        if len(data)-1<lines:
            for l in range(len(data)-1):
                r=random.randint(0,len(tmp)-1)
                print(''.join(tmp[r]))
                tmp = [i for i in tmp if i!=tmp[r]]
            print("Not enough lines")
        else:
            tmp=data[1::]
            for i in range(lines):
                r=random.randint(0,len(tmp)-1)
                print(''.join(tmp[r]))
                tmp = [i for i in tmp if i!=tmp[r]]
    


def Info(file_name):
    with open(file_name) as file:
        data=[i.split(";") for i in file.readlines()]

        for elm in data:
            if(len(elm)!=len(data[0])):
                elm.append('')
            elm[3] = elm[3][:-1:]
        print(len(data)-1, "x", len(data[0]))

        for col in range(len(data[0])):
            cnt=0
            for lin in range(1,len(data)):
                if data[lin][col] != '':
                    cnt+=1
            try: 
                int(data[1][col])
            except:
                print(data[0][col], cnt, "string")
            else:
                print(data[0][col], cnt, "integer")


def DelNaN(file_name):
    with open(file_name) as file:
        data=[i.split(";") for i in file.readlines()]

        for elm in data:
            if(len(elm)!=len(data[0])):
                elm.append('')
            elm[3] = elm[3][:-1:]

        tmp=data
        for col in range(len(data[0])):
            for lin in range(1,len(data)):
                if data[lin][col] == '':
                    tmp = [tmp[i] for i in range(len(tmp)) if i!=lin]
                    
    print(tmp)



def MakeDS(file_name):
    with open(file_name) as file:
        data=[i.split(";") for i in file.readlines()]

        for elm in data:
            if(len(elm)!=len(data[0])):
                elm.append('')
            elm[3] = elm[3][:-1:]
        

        head=data[0]
        trg_path=''
        file_name=file_name.split('/')
        for i in range(len(file_name)-1):
            trg_path+=(file_name[i] + '/')
        
        Path.mkdir(trg_path + "workdata")
        Path.mkdir(trg_path + "workdata/Learning")
        Path.mkdir(trg_path + "workdata/Testing")
        Path.touch(trg_path + "workdata/Learning/train.csv")
        Path.touch(trg_path + "workdata/Testing/test.csv")

        train = []
        tmp=data[1::]
        for j1 in range(1,int((len(data)*0.7)//1)):
            r=random.randint(1,len(tmp)-1)
            train.append(tmp[r])
            tmp = [tmp[i] for i in range(len(tmp)) if i!=r]
        test = [i for i in tmp]
        print(test)

        with open(trg_path + "workdata/Testing/test.csv",'w') as file_test:
            for h in range(len(head)):
                file_test.write(head[h] + (',' * ((h+1) != len(head))) + ('\n' * ((h+1) == len(head))))
            for ts in test:
                for i in range(len(ts)):
                    file_test.write(ts[i] + (',' * ((i+1) != len(ts))) + ('\n' * ((i+1) == len(ts))))
        
        with open(trg_path + "workdata/Learning/train.csv",'w') as file_test:
            for h in range(len(head)):
                file_test.write(head[h] + (',' * ((h+1) != len(head))) + ('\n' * ((h+1) == len(head))))
            for tr in train:
                for i in range(len(tr)):
                    file_test.write(tr[i] + (',' * ((i+1) != len(tr))) + ('\n' * ((i+1) == len(tr))))
        
