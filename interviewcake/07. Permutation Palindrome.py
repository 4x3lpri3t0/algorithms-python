def has_permutation_palindrome(text):
    unpaired_chars = set()

    for char in text:
        if char in unpaired_chars:
            unpaired_chars.remove(char)
        else:
            unpaired_chars.add(char)

    return len(unpaired_chars) <= 1


print(has_permutation_palindrome("civic"))  # True
print(has_permutation_palindrome("ivicc"))  # True
print(has_permutation_palindrome("civil"))  # False
print(has_permutation_palindrome("livci"))  # False
