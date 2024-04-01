# ------------------------------------------------------------------------
#
# Python program to print half pyramid pattern
#
# AUTHOR  : Anuhya Dasaraju
# VERSION  DATE             AUTHOR           CHANGES
# -------  ----             -------          -------
# 1.0      29th Mar, 2024   Anuhya Dasaraju  Initial version
#
# ------------------------------------------------------------------------

value = 1

for i in range(0, 5):
    for j in range(0, i+1):
        print(value,end=" ")
        value += 1
    print()
    i += 1

