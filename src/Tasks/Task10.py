# Task #10 -
# ✅ Factorial n = 5 5! -->54321 -> 120 3! -> 321 -> 6 4! -> 432*1 -> 24


num=int(input("Enter the number : "))
if num == 0 or num == 1:
    print(1)
else:
    fact=1
    for i in range(1,num+1,1):
        fact = fact * i
        print(i,fact)
    print(fact)



