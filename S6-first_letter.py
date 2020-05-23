def first_list(strs):
    """
    Given a list of strings, create and return a dictionary whose 
    keys are the unique first characters of the strings and whose 
    values are lists of words beginning with those characters, in 
    the same order that they appear in strs.

    >>> first_list(['banter', 'brahm', 'aardvark', 'python', 'antiquated'])
    {'b': ['banter'], 'a': ['aardvark', 'antiquated'], 'p': ['python']}
    """
    diction = {}
    for i in strs:
        if i[0] not in diction:
            lst = [i]
            diction[i[0]] = lst
        else:
            lst = diction[i[0]]
            lst.append(i)
            diction[i[0]] = lst
    return diction

