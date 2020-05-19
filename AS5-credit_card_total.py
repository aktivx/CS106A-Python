"""
File: credit_card_total.py
--------------------------
This program totals up a credit card bill based on
how much was spent at each store on the bill.
"""


INPUT_FILE = 'bill1.txt'


def main():
    """
    Add your code (remember to delete the "pass" below)
    """
    f = open(INPUT_FILE)
    final_dict = {}
    for line in f:
        line = line.strip()
        linelist = line.split('[')
        linelist.pop(0)
        linelist = linelist[0].split('] $')
        key = linelist[0]
        value = int(linelist[1])
        if key not in final_dict.keys():
            final_dict[key] = value
        else:
            final_dict[key] += value
    for keys in final_dict.keys():
        print(keys + ': $' + str(final_dict[keys]))

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
