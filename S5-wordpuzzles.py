#!/usr/bin/env python3


def is_tridrome(word):
    """
    Returns whether or not word is a tridrome, i.e., the first three letters
    are the same as the last three letters.

    Arguments:
        word -- The word to check

    >>> is_tridrome('ENTERTAINMENT')
    True
    >>> is_tridrome('UNDERGROUND')
    True
    >>> is_tridrome('DEFENESTRATION')
    False
    >>> is_tridrome('PYTHON')
    False
    >>> is_tridrome('')
    False
    """
    if len(word) < 6:
        return False
    if word[0] == word[len(word) - 3] and word[1] == word[len(word) - 2] and word[2] == word[len(word) - 1]:
        return True
    else:
        return False


ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def is_peaceful(word):
    """
    Returns whether a word is peaceful, i.e., whether its letters appear in
    sorted order.

    Arguments:
        word -- The word to check
    >>> is_peaceful('ABORT')
    True
    >>> is_peaceful('FIRST')
    True
    >>> is_peaceful('')
    True
    >>> is_peaceful('PYTHON')
    False
    >>> is_peaceful('CHOCOLATE')
    False
    """
    if len(word) == 0:
        return True

    index_ip = ALPHABET.find(word[0].upper())
    for i in range(1,len(word)):
        letter_i = word[i]
        letter_i = letter_i.upper()
        index_i = ALPHABET.find(letter_i)
        if index_i < index_ip:
            return False
        index_ip = index_i

    return True

def is_stacatto(word):
    """
    Returns whether a word is a stacatto word, i.e., whether the letters in
    even positions are vowels.

    Arguments:
        word -- The word to check

    >>> is_stacatto('AUTOMATIC')
    True
    >>> is_stacatto('POPULATE')
    True
    >>> is_stacatto('')
    True
    >>> is_stacatto('PYTHON')
    False
    >>> is_stacatto('SPAGHETTI')
    False
    """
    VOWELS = 'AEIOUY'
    if len(word) > 0:
        for i in range(0, len(word) - 1, 2):
            if word[i + 1] not in VOWELS:
                print
                return False
        return True
    return True


def count_tridromes(filename):
    """
    Return the number of tridromes in the file
    """
    counter_trid = 0
    f = open(filename)
    for line in f:
        line = line.strip()
        if is_tridrome(line):
            counter_trid += 1

    return counter_trid


def count_peaceful(filename):
    """
    Return the number of peaceful words in the file
    """
    counter_peac = 0
    f = open(filename)
    for line in f:
        line = line.strip()
        if is_peaceful(line):
            counter_peac += 1

    return counter_peac


def count_stacatto(filename):
    """
    Return the number of stacatto words in the file
    """
    counter_stac = 0
    f = open(filename)
    for line in f:
        line = line.strip()
        if is_stacatto(line):
            counter_stac += 1

    return counter_stac


if __name__ == "__main__":
    WORDS_FILE = "words.txt"

    print("Number of tridromes in English language: " +
          str(count_tridromes(WORDS_FILE)))
    print("Number of peaceful words in English language: " +
          str(count_peaceful(WORDS_FILE)))
    print("Number of stacatto words in English language: " +
          str(count_stacatto(WORDS_FILE)))
