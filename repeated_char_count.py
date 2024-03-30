#Write a Python program to count repeated characters in a string . Sample string: 'thequickbrownfoxjumpsoverthelazydog’.

string = input("Enter a string: ")

dict = {}
for key in string:
    if key in dict:
        dict[key] += 1
    else:
        dict[key] = 1

for k,v in dict.items():
    if v > 1:
        print(f"{k} {v}")
