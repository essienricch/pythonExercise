def dimensional_arr(arr):
    summer = 0
    for i in range(len(arr)):
        summer += arr[i][i]
    return summer


if __name__ == "__main__":
    print(dimensional_arr([[1, 2, 1], [3, 4, 6], [2, 4, 2]]))
