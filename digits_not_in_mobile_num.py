# ------------------------------------------------------------------------
#
# Python program to find the digits which are absent in a given mobile number.
#
# AUTHOR  : Anuhya Dasaraju
# VERSION  DATE             AUTHOR           CHANGES
# -------  ----             -------          -------
# 1.0      29th Mar, 2024   Anuhya Dasaraju  Initial version
#
# ------------------------------------------------------------------------
# Inputting the number
num = input("Enter a mobile number: ")

# Input validation
if len(num) == 10 and num.isnumeric():
    # If valid, printing the digits which are absent
    digits = [i for i in range(0,10)]
    mobile = [int(i) for i in num]
    print("Digits that are absent in the mobile no. are: ")
    for i in digits:
        if i not in mobile:
            print(i,end=" ")
else:
    # If input not valid giving an error
    print("Error! You need to enter a 10 digit number!")
