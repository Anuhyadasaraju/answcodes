#------------------------------------------------------------------------
#
# Python program to add, subtract, multiple and divide any two numbers
#
# AUTHOR  : Anuhya Dasaraju
# DATE    : 8th March, 2024
# VERSION : 1.0
#------------------------------------------------------------------------
print("Enter 2 numbers to perform arithmetic operations")
while True:
    num1 = input('Enter the first number: ')
    num2 = input('Enter the second number: ')

    try:
        num1 = float(num1)
        num2 = float(num2)
        break

    except ValueError:
        print('Invalid!! You need to enter a number!\n')

add = num1 + num2
rounded_subtract = round(num1 - num2, 2)
rounded_multiply = round(num1 * num2, 2)
rounded_division = round(num1 / num2, 2)

print(f"\nAddition of {num1} and {num2} is: {add}")
print(f"Subtraction of {num1} and {num2} is: {rounded_subtract}")
print(f"Multiplication of {num1} and {num2} is: {rounded_multiply}")
print(f"Division(rounded to 2 decimal places) of {num1} and {num2} is: {rounded_division}")