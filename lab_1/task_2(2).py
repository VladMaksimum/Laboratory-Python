n=int(input())
result=['1']
result[0]= (n-1) * ' ' + result[0]
step='1'

print('<',0 * ' ','>')
for i in range(1,n):
    step= str((i+1)%10) + step + str((i+1)%10)
    result.append((n-i-1) * ' ' + step)

result=result[::-1]
for j in range(n):
    print(result[j])
