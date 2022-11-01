
my_dict = {}


def rich_dict(startpoint, endpoint):
    for count in range(startpoint, endpoint + 1):
        square = count * count
        my_dict[count] = square

    print('My updated dictionary is: {}'.format(my_dict))


if __name__ == '__main__':
    numb = 4
    numb2 = 20
    rich_dict(numb, numb2)
