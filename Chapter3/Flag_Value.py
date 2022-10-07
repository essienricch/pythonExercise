# Determine the class average for the quiz with your Script

if __name__ == '__main__':
    total = 0
    count = 0
    grade1_int = 0
    print('Welcome to St Joseph High School \n Mathematics Test Grading:')
    grade_int = int(input('Enter student score ranging from 1 - 100: or Press \'-1\' to exit : '))
    if grade_int != -1:
        while grade1_int != -1:
            grade1_int = int(input('Enter student score ranging from 1 - 100: or Press \'-1\' to exit : '))
            total += grade1_int
            count = count + 1

        if count > 1:
            total += grade_int + 1
            # totale = grade1_int + total + 1
            print('Total grade input by Teacher', total)
            print('Class Average of the grades: ', total / count)

        else:
            print('Total grade input by Teacher', grade_int)
            print('Class Average of the grades: ', grade_int / 1)
            # elif grade_int > 0:
            # print('Total grade input by Teacher', total + 1)

    else:
        print('No input was taken \n Thank you for using this program!!! ')
