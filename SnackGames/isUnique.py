def is_unique(arr):
    for x in range(len(arr)):
        for y in range(len(arr)):
            if arr[x] == arr[y]:
                return False
            else:
                return True


if __name__ == "__main__":
    mon = [1, 2, 3, 4, 4]
    print(is_unique(mon))
