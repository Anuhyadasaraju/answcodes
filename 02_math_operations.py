# ------------------------------------------------------------------------
#
# Python program to add, subtract, multiple and divide any two numbers
#
# AUTHOR  : Anuhya Dasaraju
# VERSION  DATE             AUTHOR           CHANGES
# -------  ----             -------          -------
# 1.0      08th Mar, 2024   Anuhya Dasaraju  Initial version
# 1.1      10th Mar, 2024   Anuhya Dasaraju  Added input validation code
# 1.2      10th Mar, 2024   Anuhya Dasaraju  Added code for handling divide by zero error
# 1.3      12th Mar, 2024   Anuhya Dasaraju  Removed while loop for Try/Except block and added the operations in else part
#
# ------------------------------------------------------------------------
print("Enter 2 numbers to perform arithmetic operations")
# Input validation code
try:
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
except ValueError:
    print('Invalid!! You need to enter a number!\n')
else:
    # Performing the operations if inputs are correct
    # addition
    add = num1 + num2
    print(f"\nAddition : {add}")

    # subtraction rounded to 2 decimal places
    rounded_subtract = round(num1 - num2, 2)
    print(f"Subtraction (rounded to 2 decimal places) : {rounded_subtract}")

    # multiplication rounded to two decimal places
    rounded_multiply = round(num1 * num2, 2)
    print(f"Multiplication (rounded to 2 decimal places) : {rounded_multiply}")

    # division rounded to two decimal places
    # handling divide by zero error
    if num2 == 0:
        print("Can't divide by zero")
    else:
        rounded_division = round(num1 / num2, 2)
        print(f"Division (rounded to 2 decimal places) : {rounded_division}")


