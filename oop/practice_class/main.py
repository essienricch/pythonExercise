
from oop.practice_class.Restaurant import Restaurant

if __name__ == '__main__':
    restaurant = Restaurant('Mmandu-spicy', 'Continental')
    restaurant.open_restaurant()
    restaurant.describe_restaurant()
    restaurant.set_name('toro')
    name_of_restaurant = restaurant.get_name
    print(name_of_restaurant)
