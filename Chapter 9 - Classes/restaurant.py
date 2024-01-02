class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type    = cuisine_type
        self.number_served   = 0

    def describe_restaurant(self):
        print(f'The restaurant name is {self.restaurant_name} and and the cuisine type is {self.cuisine_type}.')

    def open_restaurant(self):
        print('The restaurant is opened.')

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number_served):
        if number_served < 0:
            return
        self.number_served += number_served


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        for flavor in self.flavors:
            print('Flavor: ' + flavor)
