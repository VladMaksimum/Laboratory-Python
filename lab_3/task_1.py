lst = [3,5,2,0,1]

max_i = lst.index(max(lst))
min_i = lst.index(min(lst))

tmp = lst[max_i]
lst[max_i] = lst[min_i]
lst[min_i] = tmp

print(lst)