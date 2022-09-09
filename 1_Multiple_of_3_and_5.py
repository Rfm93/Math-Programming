"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import time

start = time.time()

c = set()


# Iterate to find all multiple of 3 and 5 below 1000

for t in range(0, 1000, 3):
    c.add(t)
    for f in range(0, 1000, 5):
        c.add(f)

answer = sum(c)

print("\nThe solution of problem is {}!\n".format(answer))

# The solution of problem is 233168!

end = time.time()

print("The time of execution is {}.\n".format(end-start))

# The time of execution is 0.006984233856201172.


