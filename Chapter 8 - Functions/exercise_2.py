def make_shirt(size='L', message_on_shirt='I Love Python'):
    print(f'The shirt\'s size is {size} and the message on it is {message_on_shirt}')

make_shirt('L', 'Great shirt')
make_shirt(message_on_shirt='Great shirt', size='L')

make_shirt()
make_shirt(size='M')
make_shirt(size='S', message_on_shirt='Another message')

def describe_city(city, country='Romania'):
    print(f'{city} is in {country}')

describe_city('Brasov')
describe_city(country='United States of America', city='New York')
describe_city('Reykjavik', 'Iceland')
