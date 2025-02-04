string = input()

i=0
while(i<len(string)):
    if (ord(string[i])>=65 and ord(string[i])<=90) or (ord(string[i])>=97 and ord(string[i])<=122):
         let=string[i]
         i+=1
    else:
         string = string[:i:] + let * (int(string[i])-1) + string[i+1::]
         i+=1
print(string)