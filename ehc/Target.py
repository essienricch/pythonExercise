def count_numbers(sorted_list, less_than):
    count = 0

    for element in sorted_list:
        if less_than > element:
            count += 1
    print(count)


if __name__ == '__main__':
    my_list = [12, 15, 20, 30, 35, 40]
    target = 23
    count_numbers(my_list, target)
