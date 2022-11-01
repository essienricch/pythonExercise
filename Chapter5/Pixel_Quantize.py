def pixels_list():
    quantized_value = int(input('Enter a pixel value to get a list of the value range: '))
    start_point = quantized_value - 9
    end_point = quantized_value + 11
    list_pixel = []
    for i in range(start_point, end_point):
        list_pixel.append(i)
    print(list_pixel)


if __name__ == '__main__':
    pixels_list()
