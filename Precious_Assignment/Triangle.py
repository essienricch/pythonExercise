if __name__ == '__main__':
    print('Welcome to my program that determines an Equilateral Triangle! ')
    print()
    length = int(input('Enter first length of the triangle: '))
    length2 = int(input('Enter second length of the triangle: '))
    length3 = int(input('Enter third length of the triangle: '))

    if length == length2 == length3:
        print('This is an equilateral triangle')
    else:
        print('It is not an equilateral triangle')