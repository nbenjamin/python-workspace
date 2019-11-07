import random

# Dictionary
names = {'basic': '1997', 'fortran': '1997', 'c': '2000', 'c++': '2001', '.net': '2003', 'java': '2003',
         'python': '2019'}

year = names.get('java')

if year is None:
    print('Year is missing ')
else:
    print('Year is ', year)

# Two Dimensional Array

menus = {
    'Breakfast': ['Boiled Eggs', 'Milk'],
    'Lunch': ['Salad', 'Salmon Grill'],
    'Dinner': ['Noodles', 'Chicken Sandwich']
}
# To get Lunch items
print(menus.get('Lunch'))

# Looping

ages = [35, 40, 36, 33, 32]
total = 0
for age in ages:
    total = total + age

print('Average age is - ', format(total / len(ages), '.0f'))

for i in range(5):
    print(i)

# print starts from 20 and increment by 2 to reach 27
for y in range(20, 27, 2):
    print(y)

# Dictionary's Key/Value in loop
for program, year in names.items():
    print(program, " - ", year, sep='')

# While Loop
x = 1
while x != 3:
    print(' x = ', x)
    x += 1

# Types of Random number generation
print(random.random())
# Return a random number from [0.0 to 1.0]
print(random.choice([10, 20, 30, 40, 50]))
# Return a random number from the given list
print(random.randint(1, 500))
# Return a random number within the given range
