def ismultiple(num1, num2):
    if num2 % num1 == 0:
        print('Your second input is a multiple of the first')
        return [True]
    else:
        print('Value not a multiple of the first')
        return [False]


if __name__ == '__main__':
    ismultiple(3, 9)
