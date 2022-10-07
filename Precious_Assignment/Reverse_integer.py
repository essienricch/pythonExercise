if __name__ == '__main__':
    number = int(input('Enter an integer: '))
   # reverse = 0
    # while number > 0:
       # value = number % 10
       # reverse = reverse * 10 + value
      # number = number // 10

    val = number % 10
    val1 = number % 100 // 10
    val2 = number % 1000 // 100
    val3 = number % 10000 // 1000

    print('Reverse of your input is: ', val, val1, val2, val3)
