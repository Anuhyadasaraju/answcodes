#------------------------------------------------------------------------
#
# Python program to add, subtract, multiple and divide any two numbers
#
# AUTHOR  : Anuhya Dasaraju
# DATE    : 8th March, 2024
# VERSION : 1.0
#------------------------------------------------------------------------
print("Enter 2 numbers to perform arithmetic operations")
num1 = int(input("num1 : "))
num2 = int(input("num2 : "))

add = num1 + num2
subtract = num1 - num2
multiply = num1 * num2
divide = (num1 / num2)
rounded_division = round(divide,2)

print(f"Addition of {num1} and {num2} is: {add}")
print(f"Subtraction of {num1} and {num2} is: {subtract}")
print(f"Multiplication of {num1} and {num2} is: {multiply}")
print(f"Division(rounded to 2 decimal places) of {num1} and {num2} is: {rounded_division}")