me = {
    'name': 'Istrate',
    'last_name': 'Mihai Septimius',
    'age': 27,
    'city': 'Constanta'
}

for key, value in me.items():
    print(value)

favorite_numbers = {
    'person_1': 1,
    'person_2': 2,
    'person_3': 3,
    'person_4': 4,
    'person_5': 5
}

for key, value in favorite_numbers.items():
    print(value)

glossary = {
    'Variable':
    '''Imagine a little box labelled with a name (like "age"). You can put things in that box (like the number 25) and use it later
    in your program. Variables store information for you to use later.''',

    'Function':
    '''Think of a recipe for cookies. It's a set of instructions you follow to get a desired outcome. Functions are similar –
    they're named blocks of code that perform a specific task, often taking information (like ingredients) and producing
    something new (like delicious cookies!).''',

    'Loop':
    '''Picture a merry-go-round repeating the same song. Loops do something repeatedly until a certain condition is met.
    They're useful for tasks like printing numbers from 1 to 10 or checking every item in a list.''',

    'Conditional':
    '''Imagine a "Yes/No" question. Conditionals make decisions based on whether something is true or false. They use statements like "if age is greater than 18"
    and can change the way your program runs depending on the answer.''',

    'Data':
    '''This is the raw material, the ingredients, the information your program works with. It can be numbers, text, images, or even complex structures
    like lists and dictionaries. Data is the fuel that keeps your program running!'''
}

for key, value in glossary.items():
    print('\n')
    print(key + ': ' + '\n')
    print(value)
