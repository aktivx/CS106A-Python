"""
File: data_analysis.py
----------------------
This program read in data on cumulative infections of a disease
in different locations, and computes the number of infections
per day at each location.
"""


def load_data(filename):
    """
    The function takes in the name of a datafile (string), which
    contains data on locations and their seven day cumulative number
    of infections.  The function returns a dictionary in which the
    keys are the locations in the data file, and the value associated
    with each key is a list of the (integer) values presenting the
    cumulative number of infections at that location.
    >>> load_data('disease1.txt')
    {'Evermore': [1, 1, 1, 1, 1, 1, 1], 'Vanguard City': [1, 2, 3, 4, 5, 6, 7], 'Excelsior': [1, 1, 2, 3, 5, 8, 13]}
    """
    dict_infect = {}
    with open(filename) as f:
        for line in f:
            line = line.strip()
            line_list = line.split(',')
            key_location = line_list.pop(0)
            key_location = key_location.strip()
            for i in range(len(line_list)):
                line_list[i] = int(line_list[i].strip())
            dict_infect[key_location] = line_list

    return dict_infect


def daily_cases(cumulative):
    """
    The function takes in a dictionary of the type produced by the load_data
    function (i.e., keys are locations and values are lists of seven values
    representing cumulative infection numbers).  The function returns a
    dictionary in which the keys are the same locations in the dictionary
    passed in, but the value associated with each key is a list of the
    seven values (integers) presenting the number of new infections each
    day at that location.
    >>> daily_cases({'Test': [1, 2, 3, 4, 4, 4, 4]})
    {'Test': [1, 1, 1, 1, 0, 0, 0]}
    >>> daily_cases({'Evermore': [1, 1, 1, 1, 1, 1, 1], 'Vanguard City': [1, 2, 3, 4, 5, 6, 7], 'Excelsior': [1, 1, 2, 3, 5, 8, 13]})
    {'Evermore': [1, 0, 0, 0, 0, 0, 0], 'Vanguard City': [1, 1, 1, 1, 1, 1, 1], 'Excelsior': [1, 0, 1, 1, 2, 3, 5]}
    """
    dict_daily_cases = {}
    for key_location in cumulative:
        cumulative_list = cumulative[key_location]
        list_daily_cases = []
        for i in range(len(cumulative_list)):
            if i == 0:
                list_daily_cases.append(cumulative_list[i])
            else:
                list_daily_cases.append(cumulative_list[i] - cumulative_list[i-1])
        dict_daily_cases[key_location] = list_daily_cases

    return dict_daily_cases



def main():
    filename = 'disease1.txt'

    data = load_data(filename)
    print("Loaded datafile " + filename + ":")
    print(data)

    print("Daily infections: ")
    print(daily_cases(data))


if __name__ == '__main__':
    main()
