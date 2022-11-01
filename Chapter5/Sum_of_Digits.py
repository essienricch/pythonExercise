def sumofdigits():
    sum_it = 0
    main_int = int(input('Enter an integer of 4 digits value to get the sum of the value: '))
    while main_int != 0:
        sum_it += main_int % 10
        main_int //= 10
    print('The sum is ', sum_it)


if __name__ == '__main__':
    sumofdigits()
