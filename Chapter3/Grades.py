def class_grade():
    count = 0
    while count <= 5:
        grade = int(input('Enter a score: '))

        while 100 < grade or grade < 0:
            print("help")
            grade = int(input("Enter a valid grade score: "))

        if 90 <= grade <= 100:
            print('Passed with an A')
        elif 70 <= grade <= 89:
            print('Passed with a B')
        elif 50 <= grade <= 69:
            print('Passed with a C')
        elif 40 <= grade <= 49:
            print('Passed with a D')
        elif 0 <= grade <= 39:
            print('Passed with an F')
        # else:
        #     print('F')

        count += 1



