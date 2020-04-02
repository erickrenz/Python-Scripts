#
# fibonacci.py
# Fibonacci Numbers
#
# Created by Eric Krenz on 4/2/20.
# Copyright © 2020 Eric Krenz. All rights reserved.
#


# Outputs Fib Values with a space in between
#
# $ python
# >>> import fibonacci
# >>> fibonacci.fibValues(100)
# 0 1 1 2 3 5 8 13 21 34 55 89
#
def fibValues(n):
    a, b = 0, 1
    while a <= n:
        print(a, end = ' ')
        a, b = b, a + b
    print()


# Saves Fib Values in an Array, then outputs array
#
# $ python
# >>> import fibonacci
# >>> fibonacci.fibArray(100)
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
def fibArray(n):
    result = []
    a, b = 0, 1
    while a <= n:
        result.append(a)
        a, b = b, a + b
    return result


# Command Line Support
#
# $ python fibonacci.py 100
# 0 1 1 2 3 5 8 13 21 34 55 89
#
if __name__ == "__main__":
    import sys
    fibValues(int(sys.argv[1]))
