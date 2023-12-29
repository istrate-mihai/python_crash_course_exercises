names = ["Maria", "Ionut", "Andrei"]

# print(names[0])
# print(names[1])
# print(names[2])

# print("Hello " + names[0])
# print("Hello " + names[1])
# print("Hello " + names[2])

# modes_of_transportation = ["motorcycle", "car", "plane"]

# print(f"I would like to own a Honda {modes_of_transportation[0]}")
# print(f"I would like to own a Ford {modes_of_transportation[1]}")
# print(f"I once flew with an RyanAir {modes_of_transportation[2]}")

print("----------------------")

for name in names:
    print(f"Hello {name}, come over to dinner")

print(f"{names[0]} can't make the dinner")

names[0] = "Cezar"

print("----------------------")

for name in names:
    print(f"Hello {name}, come over to dinner")

print("I found a bigger table")

names.insert(0, "Raluca")
names.insert(2, "Daniel")
names.append("Irina")

print("----------------------")

for name in names:
    print(f"Hello {name}, come over to dinner")

print("Unfortunately I can only invite two people to dinner, because you mostly suck")

limit = 4
count = 0

print("----------------------")

while count < limit:
    name = names.pop()
    print(f"Sorry {name}, you can't come to dinner")
    count += 1

print("----------------------")

for name in names:
    print(f"Hello {name}, you are still invited to dinner")

del names[1]
del names[0]

print("My list is empty:")
print(names)

