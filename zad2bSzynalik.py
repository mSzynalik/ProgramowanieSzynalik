import random
'''
Author - Mateusz Szynalik
In this program functions 'DoubledNumbers' and 'MultipliedNumbers' display every number from list 'numbers' multiplied by 2.
'''

i = 1
numbers = []
while i <= 5:
    numbers.append(random.randint(1, 100))
    i += 1

def DoubledNumbers(numbers):
    for elem in numbers:
        print(elem * 2)

def MultipliedNumbers(numbers):
    list_of_numbers = [x * 2 for x in numbers]
    print(list_of_numbers)

DoubledNumbers(numbers)
MultipliedNumbers(numbers)