result = ['1', '1 1']
n=int(input())

for i in range(n-2):
    line=''
    for j in range(i+1):
        prev = [int(i) for i in result[i+1].split()]
        line+=' ' + str(prev[j]+prev[j+1])
    result.append('1'+line+' 1')


for i in range(n):
    print(' '*(n-i)+ result[i])
