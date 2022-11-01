s = 'doh ri meh'

print(s.upper())
print(s.capitalize())
print(s.title())

# DECIPHER CODE WORDS:
if __name__ == '__main__':
    # import string
    # word = input('Enter a word: ')
    # key_code = int(input('Enter the key to code with: '))
    # abc = string.ascii_lowercase
    # inverse = abc[key_code:] + abc[:key_code]
    # print(word.translate(str.maketrans(abc,inverse)))

    # Slicing the String:
    s = 'my name is simbi'
    t = s[:9] + 'n' + s[10:15] + 'a'
    print(s)

    b = 'we are semicolon natives'
    print(b[:17] + 'm' + b[18:18] + 'o' + b[19:])

    # Reverse the string:
    c = "madam i'm adam"
    print(c[::-1])

    # CONCATENATE using '+':
    q = "Spam" + " " + "Jeffrey"
    print(q)

    # UPPERCASE Method:
    print(t.upper())

    # TO FIND THE NUMBER OF STRING OCCURRENCE:
    print(b.find("a", 3))

    print(f'Sorry, it is a %d' % 5, 'minute walk to %s.' % 'sabo')
    print('Sorry, is it a {} minute walk to {}?'.format(5, 'sabo'))
    print()

    #  LEFT/RIGHT WIDTH ADJUSTMENT:
    print('{:>15s} is {:<10d} years old.'.format('AJAN-GBADI', 35))

    for i in range(5):
        print('{:10d} - - > {:4d}'.format(i, i ** 2))

    # FLOATING POINT PRECISION :
    import math

    print(math.pi)
    print('pi is {:.3f}'.format(math.pi))

    print()

    for j in range(1, 20, 2):
        k = '*' * j
        print(k.ljust(20))

        # print(k.center(20))

        # print(k.rjust(20))
    for j in range(1, 20, 2):
        k = '*' * j
        print(k.rjust(20))

    for j in range(1, 20, 2):
        k = '*' * j
        print(k.center(20))
    print()

    river = 'antarctic'
    target = input('input a character to find: ')
    for index in range(len(river)):
        if river[index] == target:
            print('Letter found at index: ', index)
            break

    else:
        print('Letter', target, 'not found in', river)
    print()

    river = 'mississipi'
    target = input('input a character to find: ')
    for index, letter in enumerate(river):
        #   if letter == target:
        print('Letter found at index ', index)
        break

    else:
        print('Letter', target, 'not found in', river)

    print()

    # Name Splitting:
    name = 'John Mar-wood Cleese'
    first, middle, last = name.split()
    transform = last + ", " + first + " " + middle
    print(transform)
    print(first)
    print(middle)
    print()

    s = 'ball'
    print(s[::-1])
