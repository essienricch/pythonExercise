def product_list():
    total = 0
    product1 = 2.98
    product2 = 4.50
    product3 = 9.98
    product4 = 4.49
    product5 = 6.87
    count_int = 0
    sale_attendant = ""

    print("""
Welcome to Aphrodisiac Mall Mart.
A list of products available in our store with their respective prices.
Select your choice and have it summed up.
    """)

    start_end = 0

    start_end = int(input("""
Press 1 to start this Program or
Press '0' to end this Program: """))

    while start_end != 0:

        user_input = int(input("""
    Product Category: 
        1. Gums/Jelly's ($2.98)
        2. Snacks ($4.50)
        3. Alcoholic Beverages ($9.98)
        4. Cosmetics ($4.49)
        5. Adult Play-Toys ($6.87)
    Press (1 - 5) to make your selection:
     """))

        if user_input == 1:
            print("Added Gums/Jelly's ($2.98) to your cart")
            count_int += 1
            total += product1
        elif user_input == 2:
            print("Added Snacks ($4.50) to your cart")
            count_int += 1
            total += product2
        elif user_input == 3:
            print("Added Alcoholic Beverages ($9.98) to your cart")
            count_int += 1
            total += product3
        elif user_input == 4:
            print("Added Cosmetics ($4.49) to your cart")
            count_int += 1
            total += product4
        elif user_input == 5:
            print("Added Adult Play-Toys ($6.87) to your cart")
            count_int += 1
            total += product5
        else:
            temp = input('Are you done shopping? ')
            if temp == "YES" or temp == "yes" or temp == "Yes":
                print('Your items are ready for billing  ')
                sale_attendant = input('Sales Executive: ')
                break
            else:
                continue

    if start_end == 0:
        print('No Items Purchased ')
    else:
        print(f"\n%s Attended to you" % sale_attendant.upper())
        print(f'Total Number of Items Purchased: %d' % count_int)
        print(f"The total Value of Items purchased: $%.2f" % total)


if __name__ == '__main__':
    product_list()
