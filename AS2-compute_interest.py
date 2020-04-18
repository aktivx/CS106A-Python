"""
File: compute_interest.py
-------------------------
Add your comments here.
"""


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    initial_balance = float(input('Initial balance: '))
    s_year = int(input('Start Year: '))
    s_month = int(input('Start month: '))
    e_year = int(input('End Year: '))
    if e_year >= s_year:
        e_month = int(input('End month: '))
        s_date = s_year * 13 + s_month
        e_date = e_year * 13 + e_month
        if e_date > s_date:
            int_rate = float(input('Interest rate (0 to quit): '))
            if int_rate != 0:
                while int_rate != 0:

                    date_balance = s_date
                    balance_to_date = initial_balance

                    for i in range(s_date,e_date+1):
                        if date_balance % 13 != 0:
                            print('Year ' + str(date_balance // 13) + ', month ' + str(date_balance % 13) + ' balance: ' + str(balance_to_date))
                            balance_to_date *= (int_rate + 1)
                        date_balance += 1

                    int_rate = float(input('Interest rate (0 to quit): '))

        else:
            date_error()

    else:
        date_error()


def date_error():
    print('Starting date needs to be before ending date.')


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
