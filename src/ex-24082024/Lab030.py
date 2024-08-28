def sum_of_number():
     a = 1
     b = 2
     sum = a+b
     print(sum)
     def inner_fuction():
         print("I'm inner function")
     inner_fuction()
sum_of_number()
#print(sum_of_number()) #output will be 3 and none as function not returning anything
