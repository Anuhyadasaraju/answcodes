# ------------------------------------------------------------------------
#
#  Python program to find the largest element in a list
#
# AUTHOR  : Anuhya Dasaraju
# VERSION  DATE             AUTHOR           CHANGES
# -------  ----             -------          -------
# 1.0      29th Mar, 2024   Anuhya Dasaraju  Initial version
#
# ------------------------------------------------------------------------
def largest_element(list):
    max = 0
    for i in list:
        if i > max:
            max = i

    return max

list = [1, 25, 32, 2, 5, 7, 8, 17]
element = largest_element(list)
print(element)
