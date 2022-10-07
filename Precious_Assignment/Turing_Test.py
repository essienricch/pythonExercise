if __name__ == '__main__':
    print(f'%20s' % "DELL")
    print('Welcome to Cypherx Operating System')
    print()
    answer = input('What is your Problem?  ')
    print()
    answer2 = input('Have you had this problem before (Yes or No)?  ')
    if answer2 == "yes" or answer2 == "Yes":
        print('Well, you have it again. ')
    elif answer2 == "no" or answer2 == "No":
        print('Well, you have it now. ')
