if __name__ == '__main__':

    factor_int = int(input(' \"Enter\" number to check for factor value: '))
    count = 1
    sum = 0

    # USING FOR LOOP IN RANGE WITH

    # for counter in range(1, factor_int):
    # if factor_int % counter == 0:
    #   print(counter)
    #  sum += counter

    while count < factor_int:
        if factor_int % count == 0:
            print(count, ' ')
            sum += count

        count = count + 1

    print('Your \"sum\" of factor is: ', sum)

    if sum == factor_int:
        print('your value is a perfect number')
    else:
        print('God is good')
