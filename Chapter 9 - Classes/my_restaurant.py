from restaurant import Restaurant, IceCreamStand

restaurant = Restaurant('Chez Panisse', 'California farm-to-table')
print(f'Number of served customers: {restaurant.number_served}.')
restaurant.number_served = 10
print(f'Number of served customers: {restaurant.number_served}.')
restaurant.set_number_served(20)
print(f'Number of served customers: {restaurant.number_served}.')
restaurant.increment_number_served(-20)
restaurant.increment_number_served(20)
print(f'Number of served customers: {restaurant.number_served}.')

restaurant_1 = Restaurant('Chez Panisse', 'California farm-to-table')
print(f'Name: {restaurant_1.restaurant_name}.\n')
print(f'Cuisine type: {restaurant_1.cuisine_type}.\n')
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

restaurant_2 = Restaurant('McDonald\'s', 'Fast Food')
restaurant_3 = Restaurant('The French Laundry', 'Fine dining')

restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

ice_cream_stand = IceCreamStand('Stand 1', 'Stand', ['Vanilla', 'Chocolate', 'Strawberry', 'Mint Chocolate Chip', 'Cookies and Cream'])
ice_cream_stand.display_flavors()
