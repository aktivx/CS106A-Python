"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random

CORRECT_IN_A_ROW = 3

def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    solution_counter = 0
    while solution_counter !=  CORRECT_IN_A_ROW:
        num1 = random.randint(10,99)
        num2 = random.randint(10,99)
        print('What is ' + str(num1) + ' + ' + str(num2) + ' ?')
        value = float(input('Your answer: '))
        if value == num1 + num2:
            solution_counter += 1
            print("Correct! You've gotten " + str(solution_counter) + " correct in a row.")

        else:
            print('Incorrect. The expected answer is ' + str(num1 + num2))
            solution_counter = 0

    print('Congratulations! You mastered addition.')
# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
