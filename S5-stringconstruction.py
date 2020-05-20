
def only_one_first_char_new(s):
    """This function builds up a new string adding all characters in the input string except those that are
    the same as the first char

    >>> only_one_first_char_new('abba abba abba')
    'abb bb bb'

    >>> only_one_first_char_new('Stanford')
    'Stanford'

    >>> only_one_first_char_new('')
    ''
    """
    s_list = s.split(' ')
    s_new = ''
    for y in range(len(s_list)):
        s_row = ''
        for x in range(len(s_list[y])):
            if s_list[y][x] not in s_row:
                s_row += s_list[y][x]
        s_new += s_row
        if y != len(s_list) - 1:
            s_new += ' '

    return s_new

"""
realized at the end that i was writting something else, didn't understand the requirement at first

"""


    return s_list

def only_one_first_char_keep(s):
    """This function removes all occurences of the first character except the first char itself and
    returns the udpated string

    >>> only_one_first_char_keep('abba abba abba')
    'abb bb bb'

    >>> only_one_first_char_keep('Stanford')
    'Stanford'

    >>> only_one_first_char_keep('')
    ''

    >>> only_one_first_char_keep('aaaaa')
    'a'
    """
    s_new = ''
    if len(s) > 0:
        s_new = s[0]
        for i in range(1,len(s)):
            if s[0] != s[i]:
                s_new += s[i]
    return s_new



def make_gerund(s):
    """This function adds 'ing' to the end of the given string s and returns this new word. If the given word already
    ends in 'ing' the function adds an 'ly' to the end of s instead before returning.
    >>> make_gerund('ringing')
    'ringly'
    >>> make_gerund('run')
    'runing'
    >>> make_gerund('')
    'ing'
    >>> make_gerund('ing')
    'ly'
    """
    s_new = ''
    if len(s) < 3:
        s_new = s + 'ing'
    elif s[len(s) - 1] == 'g' and s[len(s) - 2] == 'n' and s[len(s) - 3] == 'i':
        for i in range(len(s) - 3):
            s_new += s[i]
        s_new += 'ly'
    else:
        s_new = s + 'ing'

    return s_new

def put_in_middle(outer, inner):
    """This function inserts the string inner into the middle of the string outer and returns this new value
    >>> put_in_middle('Absolutely', 'freaking')
    'Absolfreakingutely'

    >>> put_in_middle('ss', 'mile')
    'smiles'

    >>> put_in_middle('hit', 'obb')
    'hobbit'
        """
    s_new = ''
    middle_index = len(outer) // 2
    for i in range(middle_index):
        s_new += outer[i]
    s_new += inner

    for i in range(middle_index, len(outer)):
        s_new += outer[i]

    return s_new




