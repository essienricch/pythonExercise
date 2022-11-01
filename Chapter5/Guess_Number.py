import random


def guess_number():
    numb_int = random.randint(1, 1000)
    guess_numb_int = 0
    count_int = 0
    while guess_numb_int != numb_int:
        guess_numb_int = int(input('Guess a number ranging from "1 - 1000": '))

        if guess_numb_int < numb_int:

            print('You Guessed low')
            count_int += 1

            temp = input('Try-Again?  ')
            if temp == 'yes' or temp == 'YES':
                continue

            else:
                print('Thank you for participating! ')
                break

        elif guess_numb_int > numb_int:
            print('Too High!!!')
            count_int += 1

            temp = input('Try-Again? ')
            if temp == "yes" or "YES":
                continue

            else:
                print('Thank you for participating! ')
                break
        else:

            print('Congratulations, You Guessed Right')
            count_int += 1
            temp = input('\nWould you like to play again? \n')
            if temp == 'Yes' or temp == 'YES':
                continue
            else:
                print('God bless You for participating ')
                break

    if count_int > 10:
        print("\nYou should be able to do better!")

    elif count_int == 10:
        print("\nAha! You know the secret! ")
    else:
        print("\nyou know the secret or you got lucky!")

    print(f"You guessed %d%%s" % count_int % " Times")


if __name__ == '__main__':
    guess_number()
