string = input()


cnt=0
i=0
while(i<len(string)-1):
    if string[i] == string[i+1]:
        cnt+=1
        string = string[:i+1:] + string[i+2::]
    elif cnt>0:
        string = string[:i+1:] + str(cnt+1) + string[i+1::]
        cnt=0
        i+=1
    else:
        i+=1

print(string)