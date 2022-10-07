import math

if __name__ == '__main__':
    box_of_egg = 6
    print(f'%d' % box_of_egg,'eggs fits in 1 box')

    # TO CALCULATE THE NUMBER OF BOX THAT WILL FIT IN 28 EGGS:
    new_box = 28 / 6
    new_few_box = math.ceil(28 / 6)
    print(f'28 Eggs fills in %.2f' % new_box,'box')

    # TO DETERMINE THE NUMBER OF EGGS TO FILL IN THE UNCOMPLETED BOX

    last_box = 6 * (new_few_box - new_box)
    print(f' Eggs to be placed in the uncompleted box: %.2f' % last_box)
    add_eggs = 6 - last_box
    print(f'The additional eggs needed to fill the last box: %.2f' % add_eggs)
