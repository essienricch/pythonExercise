import math

if __name__ == '__main__':

    # Display tables:

    print(f'%s' % "Hour" + "%25s" % "Number of Bacteria")

    # display the calculated value using LOOP (for)

    for count in range(4):
        hour = 5 * count
        print(f'%2d' % hour, '%23d' % (200 * math.pow(2, hour)))
