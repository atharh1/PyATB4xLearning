## Task #8

# ✅ Triangle Classifier:
# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.


side1 = int(input("Enter Side1 : "))
side2 = int(input("Enter Side2 : "))
side3 = int(input("Enter Side3 : "))
if side1 == 0 or side2 == 0 or side3 == 0:
    print("Invalid input")
elif side1 == side2 and side1 == side3:
    print("Its Triangle")
elif side1 == side2 and side1 != side3 or side1 != side2 and side1 == side3 or side2 == side3:
    print("Its Isosceles")
else:
    print("Its Scalene")


