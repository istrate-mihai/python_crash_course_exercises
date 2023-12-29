car_to_rent = input('What kind of car do you want: ')
print(f'Let me see if I can find you a {car_to_rent}')

number_of_people = int(input('How many people are in your dinner group: '))

if number_of_people > 8:
    print('You will have to wait for a table')
else:
    print('Your table is ready')

number = int(input('Enter a number: '))

remainder = number % 10

if remainder == 0:
    print('Your number is a multiple of 10')
else:
    print('Your number is not a multiple of 10')
