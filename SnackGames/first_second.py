def first_second(lst):

    first = lst[0]
    second = 0
    for i in range(len(lst)):
        if lst[i] > first:
            second = first
            first = lst[i]
    return [first, second]


if __name__ == "__main__":
    print(first_second([1, 2, 3, 4, 5, 10]))
