def rich_set():
    mi_nu_list = []
    global my_set, get_input
    collect_input = 0
    count_range = 0
    count = 0

    try:
        while count < 5:
            get_input = input('Enter 5 valid integers of 2 - 90 : ')
            collect_input = int(get_input)
            if collect_input < 2 or collect_input > 90:
                print('Invalid Input, try-again')
            elif 2 <= collect_input <= 90:
                mi_nu_list.insert(count_range, collect_input)
                count_range += 1
                count += 1

    except ValueError:
        print('Invalid input compared in relation to int () with base 10: {}'.format(get_input + " "))

    my_set = set(mi_nu_list)
    print(my_set)


if __name__ == '__main__':
    rich_set()
