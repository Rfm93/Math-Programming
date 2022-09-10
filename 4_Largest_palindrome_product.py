"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import time


start = time.time()

# Create the list of three alghoritms

three_alghoritms = list(range(100, 1000))

product = []

index = 0

what_number = 0

iterate = 0

# Create the list of products of two 3-digit numbers.

while index < len(three_alghoritms):
    product.append(three_alghoritms[index] * three_alghoritms[iterate])
    iterate += 1
    if iterate == len(three_alghoritms):
        what_number += 1
        iterate = what_number
        index += 1

# convert items to string

string_products = []

for result in product:
    string_products.append(str(result))

# Reverse the string to check if the numbers are equals

palindrome = []

for string_num in string_products:
    if string_num == string_num[::-1]:
        palindrome.append(string_num)


# Convert back to integers to check the highest product in the list

int_palindrome = []

for string_num in palindrome:
    int_palindrome.append(int(string_num))

find_max_palindrome = max(int_palindrome)

print("\nThe largest 3-digit palindrome is {}!.\n".format(find_max_palindrome))

# The largest 3-digit palindrome is 906609!

end = time.time() - start

print(f"The execution of program ended in {end}s.\n")

# The execution of program ended in 0.34871792793273926.

