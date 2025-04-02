import random


with open("lab_8/username.csv") as file:
    data=[i.split(";") for i in file.readlines()]
    for elm in data:
        elm[3] = elm[3][:-1:]

def Show(file_name, type='t', lines=5, separator=';'):
    with open(file_name) as file:
        data=[i.split(separator) for i in file.readlines()]
        for elm in data:
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
    


    