# ------------------------------------------------------------------------
#
# Python program to add, subtract, multiple and divide any two numbers
#
# AUTHOR  : Anuhya Dasaraju
# DATE    : 8th March, 2024
# VERSION : 1.0
# DATE    : 10th March 2024
# VERSION : 1.1 - Added input validation code
# VERSION : 1.2 - Added code for handling divide by zero error
# ------------------------------------------------------------------------
print("Enter 2 numbers to perform arithmetic operations")
# Input validation code
while True:
    num1 = input('Enter the first number: ')
    num2 = input('Enter the second number: ')

    try:
        num1 = float(num1)
        num2 = float(num2)
        break

    except ValueError:
        print('Invalid!! You need to enter a number!\n')

# addition
add = num1 + num2
print(f"\nAddition of {num1} and {num2} is: {add}")

# subtraction rounded to 2 decimal places
rounded_subtract = round(num1 - num2, 2)
print(f"Subtraction of {num1} and {num2} is: {rounded_subtract}")

# multiplication rounded to two decimal places
rounded_multiply = round(num1 * num2, 2)
print(f"Multiplication of {num1} and {num2} is: {rounded_multiply}")

# handling divide by zero error
if num2 == 0:
    print("Can't divide by zero")
    # division rounded to two decimal places
else:
    rounded_division = round(num1 / num2, 2)
    print(f"Division(rounded to 2 decimal places) of {num1} and {num2} is: {rounded_division}")


