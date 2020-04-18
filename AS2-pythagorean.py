"""
File: pythagorean.py
--------------------
Add your comments here.
"""

import math


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    print('Enter values to compute the Pythagorean theorem.')

    cathetus1 = 0
    cathetus2 = 0
    while cathetus1 <= 0:
        cathetus1 = float(input('Enter value of first cathetus: '))
        if cathetus1 <= 0:
            print('Not valid cathetus value. Retry')
        else:
            print('cathetus1 = ' + str(cathetus1))

    while cathetus2 <= 0:
        cathetus2 = float(input('Enter value of second cathetus: '))
        if cathetus2 <= 0:
            print('Not valid cathetus value. Retry')
        else:
            print('cathetus2 = ' + str(cathetus2))


    hypotenuse = math.sqrt(cathetus1**2 + cathetus2**2)

    print('hypothenuse = ' + str(hypotenuse))




# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
