import random

def prime_check(n):
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False

    for i in range(3, int(n**0.5)+2, 2):
        if n % i == 0:
            return False
    return True


def prime_gen(choice):
    min_number = 2
    max_number = 1000
    products = []
    genetating = True

    while genetating:
        if choice == 'manual':
            if len(products) < 1:
                number_gen = int(input('Provide first prime number: '))
            elif len(products) < 2:
                number_gen = int(input('Provide second prime number: '))

        elif choice == 'auto':    
            number_gen = random.randint(min_number, max_number)

        if prime_check(number_gen):
            products.append(number_gen)
        elif choice == 1:
            print(f'\n|| {number_gen} is not a prime number.\n'
                   '|| Try again.\n')

        if len(products) == 2:
            genetating = False
    return products



choice = input('Manual (1) or Auto (anything else): ')
if choice == '1':
    choice = 'manual'
else:
    choice = 'auto'

p, q = prime_gen(choice)
print(f'p: {p}\n'
      f'q: {q}')
