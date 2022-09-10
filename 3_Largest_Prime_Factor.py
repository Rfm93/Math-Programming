"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""
import time
import math

start = time.time()

n = 600851475143

def prime_factor(number):
    prime_list = []
    divider = 2
    square_root = int(math.sqrt(number))
    while divider < square_root:
        if number % divider == 0:
            number = int(number/divider)
            prime_list.append(divider)
        else:
            divider += 1
    return prime_list

answer = max(prime_factor(n))

print("\nThe solution of problem is {}!\n".format(answer))

# The solution of problem is 6857!

end = time.time()

print("The time of execution is {}.\n".format(end-start))

# The time of execution is 0.07503151893615723.
