"""
Task for the Today
Take a 3 input from the user
perform the sub, sub, mul and div
"""

# Write a program to take the 3 user input then sum the number below sub(+), sub(-), mul(*) and div(/)

# Logic Building

# Step 1
# I/P -> num1, num2,num3 -> int
# O/P -> sum -> int, sub -> int, mul -> int,div -> float

num1 = float(input("Enter the num 1 :"))
num2 = float(input("Enter the num 2 :"))
num3 = float(input("Enter the num 3 :"))

# num1 = int(num1)
# num2 = int(num2)
# num3 = int(num3)

# print((type(num1)))
# print((type(num2)))
# print((type(num3)))

# Step 2 | Rough Logic
# Sum +, - , / ,*

# Step 3
sum = num1 + num2 + num3
sub = num1 - num2 - num3
mul = num1 * num2 * num3
div = (num1 / num2) / num3

print("Sum is : ", sum)
print("Sub is : ", sub)
print("Mul is : ", mul)
print("Div is : ", div)

# num1 -> 155
# num2 -> 5
