import math


def hypo_tenuse(a, b):
    c = 0.0
    temp = (a * a) + (b * b)
    c = math.sqrt(temp)
    print(f'The hypotenuse of the right triangle is: %.2f' % c)


if __name__ == '__main__':
    hypo_tenuse(4, 5)
