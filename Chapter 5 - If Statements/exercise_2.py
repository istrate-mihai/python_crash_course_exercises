green       = 'green'
yellow      = 'yellow'
red         = 'red'

alien_color = input('Enter a color: ').strip()

if alien_color == green:
    print('You earned 5 points')
elif alien_color == yellow:
    print('You earned 10 points')
elif alien_color == red:
    print('You earned 15 points')

age = int(input('Enter your age: ').strip())

if age < 2:
    print('You are a baby')
elif age >= 2 and age < 4:
    print('You are a toddler')
elif age >= 4 and age < 13:
    print('You are a kid')
elif age >= 13 and age < 20:
    print('You are a teenager')
elif age >= 20 and age < 65:
    print('You are an adult')
elif age >= 65:
    print('You are an elder')

favorite_fruits = ['strawberries', 'mango', 'bananas']

if 'grapes' in favorite_fruits:
    print('Found grapes')

if 'kiwis' in favorite_fruits:
    print('Found kiwis')

if 'strawberries' in favorite_fruits:
    print('Found strawberries')

if 'mango' in favorite_fruits:
    print('Found mango')

if 'bananas' in favorite_fruits:
    print('Found bananas')
