def calculate_grade_score():
    grade_points = {'A': 4.0, 'B': 3.5, 'C': 3.0, 'D': 2.5, 'F': 1.5}
    total_score = 0
    number_of_course = 0
    average_score = 0
    print(' Welcome to Semi-Colon Academy Grade Calculator.\n')
    print(' Enter your grades to get your total score. \n '
          'Enter a blank space to end program. \n')

    finish = False
    while not finish:
        grade_input = input(' Input your grades: ')

        if grade_input == '':
            finish = True

        elif grade_input not in grade_points:
            print('Grade {} does not exist'.format(grade_input))

        else:
            total_score += grade_points[grade_input]
            number_of_course += 1

    print()
    print("Your total scores after summing up your grade is {0:2} ".format(total_score))

    if number_of_course > 0:
        average_score = total_score / number_of_course
        if average_score >= 3.5:
            print("Congratulations!!! You passed with an Average score of {0:2}".format(average_score))
        else:
            print('You passed with an average score of {} \n Work Harder Lad.'.format(average_score))


if __name__ == '__main__':
    calculate_grade_score()
