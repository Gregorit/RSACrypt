import random
import math

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
    max_number = 10000
    products = []
    generating = True

    while generating:
        if choice == 'manual':
            if len(products) < 1:
                number_gen = int(input('Provide first prime number: '))
            elif len(products) < 2:
                number_gen = int(input('Provide second prime number: '))
        elif choice == 'auto':    
            number_gen = random.randint(min_number, max_number)

        if prime_check(number_gen):
            products.append(number_gen)
        elif choice == 'manual':
            print(f'\n|| {number_gen} is not a prime number.\n'
                   '|| Try again.\n')

        if len(products) == 2:
            generating = False
    return products


def key_gen(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    # Generating e which will be relatively prime to phi
    while True:
        e = random.randrange(1, phi)
        if math.gcd(e, phi) == 1:
            break


    #put here method for private key
    
    return((n, e))


choice = input('Manual (1) or Auto (anything else): ')
if choice == '1':
    choice = 'manual'
else:
    choice = 'auto'

p, q = prime_gen(choice)
print(f'p: {p}\n'
      f'q: {q}')

public_key = key_gen(p, q)
print(f'Public key:\n{public_key}')
