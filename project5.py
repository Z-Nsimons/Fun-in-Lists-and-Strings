# Project 5
# CMSC 254
# <Zerlyne>
# CMSC 254 Project 5 Template

# Write your code for these functions
def has_illegal_letters(word, letters):
    count = 0
    index = len(word)
    while count < index:
        for letter in word:
            for char in letters:
                count = count + 1
                if word[count] == char:
                    return True
                else:
                    return False

def has_only_legal_letters(word, letters):
    word = word.lower()
    for char in word:
        if char != ' ' and char not in letters:
            return False
    return True

def uses_all_letters(word, letters):
    word = word.lower()
    return all(char in word for char in letters)

def is_in_abc_order(word):
    word = word.lower()
    return word == ''.join(sorted(word))

if __name__ == "__main__":
    # If implemented correctly, displays True
    print(has_illegal_letters("hello world", "eo"))

    # If implemented correctly, displays False
    print(has_illegal_letters("hello world", "abc"))

    # If implemented correctly, displays True
    print(has_only_legal_letters("Hoe alfalfa", "acefhlo"))

    # If implemented correctly, displays False
    print(has_only_legal_letters("Have alfalfa", "acefhlo"))

    # If implemented correctly, displays True
    print(uses_all_letters("Hoe alfalfa", "aefhlo"))

    # If implemented correctly, displays False
    print(uses_all_letters ("Hoe alfalfa", "acefhlo"))

    # If implemented correctly, displays True
    print(is_in_abc_order("glossy"))

    # If implemented correctly, displays False
    print(is_in_abc_order("matte"))
