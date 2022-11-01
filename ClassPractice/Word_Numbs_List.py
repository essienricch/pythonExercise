def words():
    words_str = input('Enter a word and get it arranged: ')
    word = sorted(words_str)
    print(word)


def numbers():
    nums_int = input('Enter a number and gets its sorted: ')
    num = sorted(nums_int)
    num_list = []
    for count in num:
        num_list.append(int(count))
    print(num_list)


if __name__ == '__main__':
    words()
    numbers()
