my_list=["bread","meat","eggs"]
print(my_list)
for i in my_list:
    print(i)
print(my_list[0])
my_list.append("vegetables")
print(my_list)
my_list.remove("vegetables")
print(my_list)
my_list.remove(my_list[0])
print(my_list)
my_tuple=tuple(my_list)
print(my_list)
print(my_tuple)
print(len(my_tuple))
print(my_tuple[0])
my_list[0]="insert"
print(my_tuple)
print(my_list)
my_list[1]="insert2"
print(my_list)
