"""
File: moon_weight.py
--------------------
Add your comments here.
"""

MOON_WEIGHT_COEFFICIENT = 0.165

def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    earth_weigh = float(input('Enter your weight in kg: '))
    if earth_weigh <= 0:
        print("Sorry you can't have a negative or no weight on earth if you're typing here.")

    else:
        moon_weight = earth_weigh * MOON_WEIGHT_COEFFICIENT
        print('Your weight on the moon is ' + str(moon_weight) + ' kg.')


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
