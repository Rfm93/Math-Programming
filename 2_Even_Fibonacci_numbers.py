"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms.

"""
import time

start = time.time()

a = 0

b = 0

fibonacci_list = []

# iterate to create the fibonacci sequence list!

while b < 4000000:
    if b == 0:
        fibonacci_list.append(b)
        b += 1
        fibonacci_list.append(b)
    else:
        a = b - a
        b = a + b
        if b < 4000000:
            fibonacci_list.append(b)
        else:
            break

answer = 0

# Create a for loop with a variable to sum the even numbers in the sequence

for number in fibonacci_list:
    if number % 2 == 0:
        answer += number
    else:
        pass

print("\nThe solution of problem is {}!\n".format(answer))

# The solution of problem is 4613732!

end = time.time()

print("The time of execution is {}.\n".format(end-start))

# The time of execution is 0.0019960403442382812.
