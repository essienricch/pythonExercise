class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Hello, Welcome to {self.name} Restaurant, and we serve {self.cuisine_type}. Enjoy your Meal.')

    def open_restaurant(self):
        print(f'{self.name} is open')
