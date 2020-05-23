LEXICON = 'dictionary.txt'

def file_to_list(filename):
    with open(filename) as f:
        file_list = []
        for line in f:
            line = line.strip()
            file_list.append(line)
    return file_list




def main():
    while True:
        word = input('Word: ')
        if word == '':
            break
        word_sorted = sorted(word)
        file_list = file_to_list(LEXICON)
        anagrams = []
        for item in file_list:
            if len(word) == len(item):
                item_sorted = sorted(item)
                if word_sorted == item_sorted:
                    anagrams.append(item)
        if anagrams == []:
            print(word + ' is not in the dictionary')
        else:
            print(anagrams)


if __name__ == "__main__":
    main()
