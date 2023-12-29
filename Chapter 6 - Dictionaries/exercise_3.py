people = [
    {
        'name': 'Istrate',
        'last_name': 'Mihai Septimius',
        'age': 27,
        'city': 'Constanta'
    },
    {
        'name': 'Martin',
        'last_name': 'Irina',
        'age': 26,
        'city': 'Constanta'
    },
    {
        'name': 'Sichim',
        'last_name': 'Ada',
        'age': 30,
        'city': 'Constanta'
    },
]

for person in people:
    print(f'The person\'s name is {person['name']} {person['last_name']}, their age is {person['age']} and they live in {person['city']}')

pets = [
    {
        'type': 'cat',
        'owner': 'Bogdan'
    },
    {
        'type': 'dog',
        'owner': 'Catalin'
    },
    {
        'type': 'hamster',
        'owner': 'Gabriel'
    },
]

for pet in pets:
    print(f'The pet is a {pet['type']}, their owner is {pet['owner']}')


favorite_places = {
    'person_1': ['place A', 'place B', 'place C'],
    'person_2': ['place D', 'place E', 'place F'],
    'person_3': ['place G', 'place H', 'place I']
}

for person, favorite_place_list  in favorite_places.items():
    print(person + ' has the following favorite places:\n')
    for favorite_place in favorite_place_list:
        print(favorite_place + '\n')

favorite_numbers = {
    'person_1': [1, 2, 3],
    'person_2': [4, 5, 6],
    'person_3': [7, 8, 9],
    'person_4': [10, 11, 12],
    'person_5': [13, 14, 15]
}

for person, favorite_number_list in favorite_numbers.items():
    print(person + ' has the following favorite numbers:\n')
    for favorite_number in favorite_number_list:
        print(str(favorite_number) + '\n')

cities = {
    'Tokyo': {
        'population': '37.34 million',
        'country': 'Japan',
        'fact':
        '''Home to the Shibuya Crossing, the busiest pedestrian crossing in the world,
        with over 2,500 people crossing every time the light changes!'''
    },

    'London': {
        'population': '8.98 million',
        'country': 'United Kingdom',
        'fact': 'Houses the world\'s oldest parliament, still in use, the Palace of Westminster, which dates back to the 11th century.'
    },

    'New York City': {
        'population': '8.82 million',
        'country': 'United States',
        'fact': 'Nicknamed "The City That Never Sleeps" due to its 24/7 activity and vibrant nightlife.'
    }
}

for city, city_properties in cities.items():
    print(f'City name is {city}, and we have the following information about it:\n')
    for city_property, city_property_value in city_properties.items():
        print(city_property.title() + ': ' + city_property_value)
    print('\n')

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },

    'eschrödinger': {
        'first': 'erwin',
        'last': 'schrödinger',
        'location': 'vienna'
    }
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

