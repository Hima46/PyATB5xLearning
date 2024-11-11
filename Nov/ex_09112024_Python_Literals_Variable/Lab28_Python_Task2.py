"""
Task for the Today - Take a 2 input from the user and Print the Quotient and Remainder
15 ->  num1
2 -> num2
Q -> 7
R -> 1
"""

# Step 1
# I/P -> num1, num2-> int
# O/P -> Quotient - > float and Remainder -> float

num1 = int(input("Enter the num 1 :"))
num2 = int(input("Enter the num 2 :"))

# Step 2 | Rough Logic (/,%)
# Step 3
mul = num1 / num2
div = num1 % num2

print("Quotient is : ", mul)
print("Remainder is : ", div)
