def read_dict_from_file(filename):
    """
    >>> read_dict_from_file('recipe.txt')
    {'flour': 200, 'salt': 2.5}
    """
    with open(filename) as f:
        file_dict = {}
        for line in f:
            line = line.strip()
            line_list = line.split(':: ')
            file_dict[line_list[0]] = line_list[1]
    return file_dict


def can_make(recipe, pantry):
    for key in recipe:
        required = float(recipe[key])
        available = float(pantry[key])

        if required > available:
            print("You can't make that recipe")
            return False
    return True


def make_recipe(recipe, pantry):
    if can_make(recipe, pantry):
        for key in recipe:
            pantry[key] = float(pantry[key]) - float(recipe[key])
        print('You can make that recipe! Your pantry now look like this: ')
        print(pantry)
        print()
    return pantry


def main():
    pantry_file = input('Enter pantry name: ')
    pantry = read_dict_from_file(pantry_file)
    receipe_file = 'receipe'
    while receipe_file != '':
        receipe_file = input('What recipe should we bake next(Press enter to quit.)? ')
        if receipe_file == '':
            break

        recipe = read_dict_from_file(receipe_file)
        make_recipe(recipe, pantry)


if __name__ == "__main__":
    main()
