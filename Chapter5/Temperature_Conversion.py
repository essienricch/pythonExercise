def temp_kelvin():
    int_celsius = float(input('Enter temperature in celsius(C) to get its Kelvin equivalent: '))
    kelvin = float(int_celsius + 273.15)
    print(kelvin, 'Kelvin')


def temp_celsius():
    int_kelvin = float(input('Enter temperature in kelvin(K) to get its Celsius equivalent: '))
    celsius = float(int_kelvin - 273.15)
    print(f'%.2f%%s' % celsius % ' Celsius')


if __name__ == '__main__':
    temp_celsius()
    temp_kelvin()
