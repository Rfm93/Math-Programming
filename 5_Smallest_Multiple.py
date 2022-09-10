"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import time 

start = time.time()

divider = 1

number = 2520

while divider <= 20:
    if number % divider == 0:
        divider += 1
    else:
        divider = 1
        number += 1

print("The solution of problem is {}".format(number))

# The solution of problem is 232792560

end = time.time()

print(f'The time of execution is {end-start}')

# The time of execution is 98.60287427902222
