from math import pi

if __name__== '__main__':
    radius_str = input("Enter the radius of your circle: ")
    radius_int = int(radius_str)

    circumference = 2 * pi * radius_int
    area = pi * (radius_int ** 2)

    print("The circumference of your input is:", round(circumference, 2),  "\n and the area is: ", round(area,2))
















