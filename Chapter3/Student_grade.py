if __name__ == '__main__':
    student = [98,76,71,87,83,90,57,79,82,94]
    total = 0
    counter = 10

    for count in student:
        total += count
    print(total)
    print(f'Average of the class: ', {total / counter})