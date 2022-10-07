if __name__ == '__main__':

    # This program would determine if your input is a palindrome number
    # A palindrome number is a number that is same after reverse

    number = int(input('Enter an number: '))
    temp = number
    reverse = 0
    while number > 0:
        value = number % 10
        reverse = reverse * 10 + value
        number = number // 10

    if temp == reverse:
        print('Your input is a Palindrome value! ')
    else:
        print('It is not a palindrome value')
