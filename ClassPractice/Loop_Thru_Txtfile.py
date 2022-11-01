def textfile():
    str_file = open("letter.txt", "w+")
    print("Pain is finally Over", file=str_file)
    str_file.close()


if __name__ == '__main__':
    textfile()
