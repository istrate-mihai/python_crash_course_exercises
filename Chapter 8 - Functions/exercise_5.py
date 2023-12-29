def sandwich_summary(*ingredientList):
    for ingredient in ingredientList:
        print(ingredient + '\n')
    print('-----------------------------')

sandwich_summary('Roast beef', 'cucumber')
sandwich_summary('Bahn Mi pork', 'kimchi', 'Sriracha mayo', 'caramelized onions')
sandwich_summary('Grilled pineapple and brie', 'figs', 'Fig jam', 'balsamic glaz', 'cranberry sauce')

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('mihai', 'istrate', location='constanta', field='informatics', salary='2000 euros')

print(user_profile)

def make_car(manufacturer, car_name, **details):
    details['manufacturer'] = manufacturer
    details['car_name']     = car_name
    return details

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
