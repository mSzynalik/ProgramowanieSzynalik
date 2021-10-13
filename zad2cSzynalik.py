import random
'''
Author - Mateusz Szynalik
In this program the 'for' loop iterates on list 'numbers' which contains 10 numbers and displays only even elements.
'''

i = 1
numbers = []
while i <= 10:
    numbers.append(random.randint(1, 100))
    i += 1

for x in range(len(numbers)):
    if numbers[x] % 2 == 0:
        print(numbers[x])