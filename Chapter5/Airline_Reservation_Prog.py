def airline_program():
    global to_continue
    sosoliso_airlist = []
    print(sosoliso_airlist)

    print('Welcome to Soso-Liso AirLine (God is our captain), First class and Economy seat available for bookings')
    class_allocate = int(input('Press 1 for First Class booking or 2 for Economy: '))
    if class_allocate == 1:
        for f in range(1, 6):
            sosoliso_airlist.append(f)
            print('Boarding Pass: Seat Number {} allocated in the First Class'.format(f))
            to_continue = int(input('Press 1 for more reservation in the first class or 2 to exit: '))
            if to_continue == 2:
                break
        if to_continue != 2:
            print('First Class Seat all booked')
            trans = int(input('Press 1 to book a seat in the economy class or 2 to end your booking: '))
            if trans == 1:
                for e in range(6, 11):
                    sosoliso_airlist.append(e)
                    print('Boarding Pass: Seat Number {} allocated in the Economy Class'.format(e))
                    to_continue = int(input('Press 1 to book more seat in the Economy class or 2 to exit: '))
                    if to_continue == 2:
                        break
        else:
            print('User booking completed')
    elif class_allocate == 2:
        for e in range(6, 11):
            sosoliso_airlist.append(e)
            print('Boarding Pass: Seat Number {} allocated in the Economy Class'.format(e))
            to_continue = int(input('Press 1 for more reservation in the Economy class or 2 to exit: '))
            if to_continue == 2:
                break
        print('Economy Class Seat all booked')
        trans = int(input('Press 1 to reserve a seat in the first class or 2 to end your booking: '))
        if trans == 1:
            for f in range(1, 6):
                sosoliso_airlist.append(f)
                print('Boarding Pass: Seat Number {} allocated in the First Class'.format(f))
                to_continue = int(input('Press 1 to book more seat in the First class or 2 to exit: '))
                if to_continue == 2:
                    break
        else:
            print('User booking completed')
    else:
        print('No booking made')
        print(sosoliso_airlist)

    if class_allocate == 1 or class_allocate == 2:
        print('List of Seat Number booked and ready to en-route: ')
        print(sosoliso_airlist)


if __name__ == '__main__':
    airline_program()
