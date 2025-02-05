
dict = {1:"один",2:"два",3:"три",4:"четыр",5:"пят",6:"шест",7:"сем",8:"восем",9:"девят",10:"десят",0:" "}
spec= {4:"четыре",11:"одинадцать",12:"двенадцать", 20:"двадцать", 40:"сорок",30:"тридцать",90:"девяносто", 100:"сто",\
        200:"двести", 300:"триста", 400:"четыреста", 1000:"тысяча"}
def do_10(n):
    if n<=10 and n>5:
       return dict[n]+"ь"
    elif n==4:
        return spec[n]
    elif n>=1 and n<=3:
        return dict[n]

def do_100(n):
    if n==11 or n==12 or n==20 or n==40 or n==30 or n==90:
        return spec[n]
    elif n>=13 and n<=19:
        return dict[n%10]+"надцать"
    elif (n>=21 and n<=29) or (n>=41 and n<=49) or (n>=31 and n<=39) or (n>=91 and n<=99):
        return spec[n-n%10] + " " + str(do_10(n%10))
    return dict[n//10]+"ьдесят " + str(do_10(n%10))

def do_1000(n):
    if n==100 or n==200 or n==300 or n==400 or n==1000:
        return spec[n]
    elif n>=100 and n<=400:
        return spec[n-n%100] + " " + str(do_100(n%100))
    return dict[n//100] + "ьсот " + str(do_100(n%100))

n=int(input())
if n<=10:
    print(do_10(n))
elif n<100:
    print(do_100(n))
elif n<=1000:
    print(do_1000(n))



