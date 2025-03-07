dict = {'Hello' : 'Hi', 'Bye' : 'Goodbye', 'List' : 'Array'};
#dict = {'beep' : 'car'};
#dict = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5};

value = input("Значение: ")
#value = int(input("Значение: "))

for i in dict:
    if dict[i] == value:
        print(i)
        break