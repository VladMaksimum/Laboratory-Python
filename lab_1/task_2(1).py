n=int(input())
result=[]
step=''

for i in range(n):
    step+=str((i+1)%10)
    result.append(step)

result=result[::-1]
for j in range(n):
    print(result[j])

