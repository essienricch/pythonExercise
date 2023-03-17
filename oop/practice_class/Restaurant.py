class Restaurant:

    def __init__(self, name, cuisine_type):
        self._name = name
        self.cuisine_type = cuisine_type

    @property
    def get_name(self):
        print(self._name)
        return self._name

    def set_name(self, name):
        self._name = name

    def describe_restaurant(self):
        print(f'Hello, Welcome to {self._name} Restaurant, and we serve {self.cuisine_type}. Enjoy your Meal.')

    def open_restaurant(self):
        print('{} is open'.format(self._name))
