list_values = ['one', 'two', 'Three', 'four', 'Five', 'six', 'seven']
list_keys = [1, 2, 3, 4, 5, 6, 7]
my_dict = {}
get_keys = ''


def list2dict():
    global my_dict, list_keys, list_values, get_keys
    for element in list_keys:
        for value in list_values:
            my_dict.setdefault(element, value)
    print(my_dict)


if __name__ == '__main__':
    list2dict()
