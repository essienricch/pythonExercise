def index_return(listy, target):
    for x in range(len(listy)):
        if listy.index(x) + listy.index(x) == target:
            sore = []
            sore.append(listy.index(x))
            return sore


if __name__ == "__main__":
    print(index_return([1, 2, 2, 1], 3))
