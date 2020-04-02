#
# prime_numbers.py
# Prime Numbers
#
# Created by Eric Krenz on 4/2/20.
# Copyright © 2020 Eric Krenz. All rights reserved.
#


# Outputs Prime Numbers with a space in between
#
# $ python
# >>> import prime_numbers
# >>> prime_numbers.primeValues(50)
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
#
def primeValues(n):
    for a in range(0, n + 1):
        if a > 1:
            for n in range(2, a):
                if (a % n) == 0:
                    break
            else:
                print(a, end = ' ')
    print()

# Saves Prime Numbers in an Array, then outputs array
#
# $ python
# >>> import prime_numbers
# >>> prime_numbers.primeArray(50)
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
#
def primeArray(n):
    result = []
    for a in range(0, n + 1):
        if a > 1:
            for n in range(2, a):
                if (a % n) == 0:
                    break
            else:
                result.append(a)
    return result


# Command Line Support
#
# $ python prime_numbers.py 50
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
#
if __name__ == "__main__":
    import sys
    primeValues(int(sys.argv[1]))
