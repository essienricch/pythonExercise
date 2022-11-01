def reverse():
    rev = input('input a string to check if it is a palindrome: ')
    if rev == rev[::-1]:
        print(rev, 'is a palindrome')
    else:
        print(rev, 'is not a palindrome')


if __name__ == '__main__':
    reverse()
