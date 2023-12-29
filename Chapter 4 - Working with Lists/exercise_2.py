for number in range(1, 21):
    print(number)

large_number_list = list(range(1, 10 ** 6 + 1))

for number in large_number_list:
    print(number)

print(large_number_list)

min_number  = min(large_number_list)
max_number  = max(large_number_list)
sum_numbers = sum(large_number_list)

print('Min is', min_number, ', max is', max_number, 'and sum total is', sum_numbers)

odd_number_list = list(range(1, 20, 2))

for odd_number in odd_number_list:
    print(odd_number)

multiple_number_list = list(range(3, 31, 3))

for multiple_number in multiple_number_list:
    print(multiple_number)

for number in range(1, 11):
    print(number ** 3)

cube_list = [number ** 3 for number in range(1, 11)]

for cube in cube_list:
    print(cube)
