prompt = 'Enter a pizza toping\n'
prompt += 'Press "quit" to close the order: '

active = True

while active:
    msg = input(prompt)
    if msg == 'quit':
        active = False
    else:
        print('We will add ' + msg + ' to the pizza')

prompt = 'What is your age\n'
prompt += 'Press "quit" to close the order: '

while True:
    msg = input(prompt)

    if msg == 'quit':
        break
    else:
        msg = int(msg)

    if msg < 3:
        print('The ticket is free')
    elif msg >= 3 and msg <= 12:
        print('The ticket is $10')
    elif msg > 12:
        print('The ticket is $15')

x = 0

while x < 5:
    print('Endless loop')
