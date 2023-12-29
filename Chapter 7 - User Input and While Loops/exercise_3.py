sandwich_orders     = ['Monte Cristo', 'Pastrami', 'Ban Mi', 'Muffuletta', 'Pastrami', 'Reuben', 'Pastrami', 'Katsu Sando']
finished_sandwiches = []

print('The deli has ran out of Pastrami')

while 'Pastrami' in sandwich_orders:
     sandwich_orders.remove('Pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print('I made your ' + sandwich + ' sandwich')
    finished_sandwiches.append(sandwich)

print('The sandwiches that were made are: \n')

for sandwich in finished_sandwiches:
    print('• ' + sandwich)

prompt_1 = 'What is your name: \n'
prompt_2 = 'What is your dream vacation\n'
prompt_2 += 'Press "quit" to close the prompt: '

poll_results = {}

active = True

while active:
    name     = input(prompt_1)
    response = input(prompt_2)

    if name == 'quit' or response == 'quit':
        active = False
    else:
        poll_results[name] = response

for name, response in poll_results.items():
    print(f"{name} would like to go to {response}.")
