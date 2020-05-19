"""
File: word_guess.py
-------------------
Fill in this comment.
"""


import random


LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with


def play_game(secret_word):
    """
    Add your code (remember to delete the "pass" below)
    """

    hiden_word = []
    for i in range(len(secret_word)):
        hiden_word.append('-')
    print('The word now looks like this: ' + list_to_string(hiden_word))

    win_status = False
    guesses_left = INITIAL_GUESSES
    while guesses_left > 0 and win_status == False:
        print('You have ' + str(guesses_left) + ' left')
        ch = input('Type a single letter here, then press enter: ')
        while len(ch) > 1 or len(ch) == 0:
            print('Guess should only be a single character.')
            print('The word now looks like this: ' + list_to_string(hiden_word))
            print('You have ' + str(guesses_left) + ' left')
            ch = input('Type a single letter here, then press enter: ')
        ch = ch.upper()
        if ch not in secret_word:
            print("There are no " + ch + "'s in the word")
            guesses_left -= 1
            if guesses_left < 1:
                break
            print('The word now looks like this: ' + list_to_string(hiden_word))

        else:
            print('That guess is correct.')
            for i in range(len(secret_word)):
                if secret_word[i] == ch:
                    hiden_word[i] = ch
            win_status = check_status(hiden_word)
            if not win_status:
                print('The word now looks like this: ' + list_to_string(hiden_word))

    if win_status:
        print('Congratulations, the word is: ' + secret_word)
    else:
        print('Sorry, you lost. The secret word was: ' + secret_word)

def check_status(hiden_word):
    if '-' in list_to_string(hiden_word):
        return False
    else:
        return True

def list_to_string(list):
    """
    >>> list_to_string(['are', 're', 'ew', 'test'])
    'arereewtest'
    """
    list_string = ''
    for i in list:
        list_string += i
    return list_string

def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """
    f = open('Lexicon.txt')
    word_list = []
    for line in f:
        line = line.strip()
        word_list.append(line)

    index = random.randrange(len(word_list))
    return word_list[index]


def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()