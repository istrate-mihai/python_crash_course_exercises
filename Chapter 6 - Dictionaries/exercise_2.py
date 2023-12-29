rivers = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Yangtze': 'China'
}

for river in rivers:
    print(f'The {river} runs through {rivers[river]}')

for river in rivers:
    print(river)

for country in rivers.values():
    print(country)

poll_users = ['jen', 'paul', 'michael', 'phil', 'thomas', 'bruce']

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for poll_user in poll_users:
    if poll_user in favorite_languages:
        print('Thank you for taking the poll')
    else:
        print('Please, take the poll')
