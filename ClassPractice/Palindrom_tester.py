def palindrome():
    import string
    original_str = input('Input a string: ')
    modify_str = original_str.lower()

    bad_chars = string.whitespace + string.punctuation

    for char in modify_str:
        if char in bad_chars:
            modify_str = modify_str.replace(char, ' ')

    if modify_str == modify_str[::-1]:
        print('''The original string is: {} 
        The modified string is: {}
        The reversal is: {}\n'''.format(original_str, modify_str, modify_str[::-1]),
              original_str, 'is a palindrome')
    else:
        print('''The original string is:  {}
            The modified string is: {}
            The reversal is: {}\n'''.format(original_str, modify_str, modify_str[::-1]),
              original_str, 'is not a palindrome')


if __name__ == '__main__':
    palindrome()
