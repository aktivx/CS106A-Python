"""
File: hailstones.py
-------------------
This is a file for the optional Hailstones problem, if
you'd like to try solving it.
"""


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    n = int(input('Enter number: '))
    n_steps = 0
    while n !=1:

        if n % 2 == 0:
            n_temp = int(n / 2)
            print(str(n) + ' is even, so I make half: ' + str(n_temp))
            n = n_temp

        else:
            n_temp = 3 * n + 1
            print(str(n) + ' is odd, so I make 3n + 1: ' + str(n_temp))
            n = n_temp

        n_steps +=1

    print('The process took ' + str(n_steps) + ' steps to reach 1')


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
