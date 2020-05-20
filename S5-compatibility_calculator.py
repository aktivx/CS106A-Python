def in_common(l1, l2):
    """
    >>> in_common(['a', 'b', 'c', 'd'], ['c', 'd', 'm', 'n', 'x', 'z'])
    0.2
    """
    comon_counter = 0
    for i in l1:
        if i in l2:
            comon_counter += 1
    comon_value = comon_counter / (len(l1) + len(l2))
    return comon_value


def calc_score(netflix_history1, netflix_history2, fav_books1, fav_books2):

    score = in_common(netflix_history1, netflix_history2) + in_common(fav_books1, fav_books2)
    return score


def new_friend(name_list, compatibility_scores):
    """
    >>> name_list = ['Michelle', 'Joe', 'Joe2']
    >>> compatibility_scores = [0.9, 0.1, 0.9]
    >>> new_friend(name_list, compatibility_scores)
    ['Michelle', 1]
    """
    max_element = max(compatibility_scores)
    print(max_element)
    index = compatibility_scores.index(max_element)
    print(index)
    new_friend_list = [name_list[index], max_element]
    return new_friend_list