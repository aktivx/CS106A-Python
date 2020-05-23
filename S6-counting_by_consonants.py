VOWELS = ['A', 'E', 'I', 'O', 'U']

def count_by_consonants(filename):
    """
    Reads in the file whose name is filename and returns a dictionary
    that contains counts of words that share the same consonants in order.
    """

    with open(filename) as f:
        file_list = []
        for line in f:
            line = line.strip()
            file_list.append(line)
    file_dict = {}
    for i in file_list:
        word = i
        vowel_free_word = ''
        for a in range(len(word)):
            if word[a].upper() not in VOWELS:
                vowel_free_word += word[a]

        if vowel_free_word not in file_dict:
            file_dict[vowel_free_word] = 1
        else:
            file_dict[vowel_free_word] += 1

    return file_dict



def main():
    filename = input("Filename: ")
    print(count_by_consonants(filename))


if __name__ == "__main__":
    main()
