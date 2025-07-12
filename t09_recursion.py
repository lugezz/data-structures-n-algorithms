"""
Recursion = When a thing is defined in terms of itself. - Wikipedia
Apply the result of a procedure, to a procedure.

A recursive method calls itself. Can be a substitute for iteration.
Divide a problem into sub-problems of the same type as the original.
Commonly used with advanced sorting algorithms and navigating trees

Advantages
----------
easier to read/write
easier to debug

Disadvantages
----------
sometimes slower
uses more memory
"""


def walk(steps: int):
    """ Walks a number of steps recursively. """
    if steps < 1:
        # Base case: if no steps left, stop recursion
        return
    print("You take a step!")
    # Recursive case
    walk(steps - 1)


def factorial(num: int):
    """ Calculates the factorial of a number recursively. """
    # Base case: if num is less than 1, return 1
    if num < 1:
        return 1
    # Recursive case: multiply num by the factorial of (num - 1)
    return num * factorial(num - 1)


def power(base: int, power_v: int):
    """ Calculates the power of a number recursively. """
    # Base case: if power is less than 1, return 1
    if power_v < 1:
        # Any number to the power of 0 is 1
        return 1

    # Recursive case: multiply base by the power of (base, power - 1)
    # Because power_v is the exponent, we reduce it by 1 each time
    # For example, power(2, 3) = 2 * power(2, 2)
    # So we have 2 * 2 * 2 = 8
    return base * power(base, power_v - 1)


walk(5)
print(factorial(7))
print(power(2, 8))
