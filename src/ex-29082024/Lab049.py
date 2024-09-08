my_set={1,2,3,4,6,5,4,6}
print(my_set)
my_list=[1,1,1,2,3,4,4,]
print(my_list)
new_set=set(my_list)
print(new_set)
new_set.remove(1)
print(new_set)
new_set.add(9)
print(new_set)
#new_set[0]=1 #error
print(new_set)
new_set.clear()
print(new_set)
my_list=new_set.copy()
print(my_set)
