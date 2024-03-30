# ------------------------------------------------------------------------
#
# Python program to find the longest word in given paragraph?
#
# AUTHOR  : Anuhya Dasaraju
# VERSION  DATE             AUTHOR           CHANGES
# -------  ----             -------          -------
# 1.0      29th Mar, 2024   Anuhya Dasaraju  Initial version
#
# ------------------------------------------------------------------------
# Input
paragraph = input("Enter a paragraph: ")

words = paragraph.split()
max_len = 0

for word in words:
    if len(word) > max_len:
        max_len = len(word)
        max_len_word = word

print(f"Longest word is : {max_len_word}")