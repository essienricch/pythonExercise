def missing_value(number1):
    for x in range(len(number1)):
        if x not in number1:
            return x


if __name__ == "__main__":
    number = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10]
    # missing_value(number)
    print(missing_value(number))
