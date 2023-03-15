def search_insert(arr, target):
    for i in range(len(arr)):
        if target == arr[i]:
            return i
        else:
            if arr[i] > target:
                return i
    else:
        return len(arr)


if __name__ == "__main__":
    print(search_insert([1, 2, 3, 4], 5))