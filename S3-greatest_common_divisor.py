
def greatest_common_divisor(a, b):
    """
    Return the greatest common divisor of a and b.

    >>> greatest_common_divisor(4, 16)
    4
    >>> greatest_common_divisor(16, 4)
    4
    >>> greatest_common_divisor(9, 24)
    3
    >>> greatest_common_divisor(9, 24)
    3
    >>> greatest_common_divisor(3, 13)
    1
    """
    if a <= b:
        lower = a
    else:
        lower = b

    for i in range(lower, 0, -1):
        if a % i == 0 and b % i == 0:
            gcd = i
            break
    return gcd


def lowest_common_multiple(a, b):
    """
    Return the lowest common multiple of a and b.

    >>> lowest_common_multiple(2, 12)
    12
    >>> lowest_common_multiple(13, 3)
    39
    >>> lowest_common_multiple(3, 6)
    6
    >>> lowest_common_multiple(1, 3)
    3
    >>> lowest_common_multiple(6, 9)
    18
    """
    if a <= b:
        higher = b
    else:
        higher = a

    for i in range(higher, (a * b) + 1):
        if i % a == 0 and i % b == 0:
            lcm = i
            break
    return lcm


def main():
    num_1 = int(input("num 1: "))
    num_2 = int(input("num 2: "))
    print(greatest_common_divisor(num_1, num_2))
    print(lowest_common_multiple(num_1,num_2))
