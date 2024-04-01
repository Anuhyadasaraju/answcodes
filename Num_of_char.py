


def num_of_char(word):
    char_count = {}
    for key in word:
        if key in char_count:
            char_count[key] += 1
        else:
            char_count[key] = 1
    return char_count


word = input("Enter a string: ")
result = num_of_char(word.lower())
print(result)