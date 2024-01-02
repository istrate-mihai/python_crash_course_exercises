from random import randint, choice

from die import Die

my_die_6_sides  = Die()
my_die_10_sides = Die(10)
my_die_20_sides = Die(20)

for turn in range(1, 11):
    my_die_6_sides.roll_die()
    my_die_10_sides.roll_die()
    my_die_20_sides.roll_die()

my_ticket = []

def generate_lottery():
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lottery_chars  = []
    selected_chars = []

    for i in range(1, 6):
        lottery_chars.append(choice(uppercase_letters))

    for i in range(1, 11):
        lottery_chars.append(randint(1, 9))

    for i in range(1, 5):
        selected_chars.append(choice(lottery_chars))

    return selected_chars

selected_chars = generate_lottery()
print('Any ticket matching these wins a prize: ', selected_chars)

count_iteration = 0

while True:
    count_iteration += 1
    my_ticket = generate_lottery()

    if my_ticket == selected_chars:
        break

print('Iteration count to win was: ' + str(count_iteration))
