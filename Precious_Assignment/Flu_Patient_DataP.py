if __name__ == '__main__':
    total = 0
    largest = 0
    smallest = 10000000

    for count in range(7):
        infected_person = int(input('Input Number of reported infections per day: '))
        total += infected_person
        if infected_person > largest:
            largest = infected_person
        if infected_person < smallest:
            smallest = infected_person

        average_input = total / 7
    print()
    print('Total number of infected patients after one week: ', total)
    print()
    print(f'Average number of infected patients after one week: %.2f' % average_input)
    print()
    print('Smallest number of infected patients after one week: ', smallest)
    print()
    print('Largest number of infected patients after one week: ', largest)
