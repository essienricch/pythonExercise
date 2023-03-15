# CONSTANT TIME(1):
def get_first(listed):
    print(listed[2])


if __name__ == "__main__":
    my_list = [4, 6, 7, 9, 10]
    get_first(my_list)


# LINEAR TIME(N):
def get_sum(lister):
    sum_of_list = 0
    for item in lister:
        sum_of_list += item
    print(sum_of_list)


if __name__ == "__main__":
    my_list = [4, 6, 7, 9, 10]
    get_sum(my_list)


# QUADRATIC TIME (N2):
def getme_sum(mylist):
    mysum = 0
    for row in mylist:
        for item in row:
            mysum += item

    print(mysum)


if __name__ == "__main__":
    my_list = [[4, 6], [7, 9, 10]]
    getme_sum(my_list)


# LOGARITHM COMPLEXITY (LOG(N)):
def binary_search(mylist, numb):
    first_value = 0
    last_value = len(mylist) - 1
    found_flag = False

    while first_value <= last_value and not found_flag:
        mid = (first_value + last_value) // 2
        if mylist[mid] == numb:
            found_flag = True
        else:
            if numb < mylist[mid]:
                last_value = mid - 1
            else:
                first_value = mid + 1
    print(found_flag)


if __name__ == "__main__":
    my_list = [4, 12, 7, 9, 10]
    numb = 6
    binary_search(my_list, numb)
