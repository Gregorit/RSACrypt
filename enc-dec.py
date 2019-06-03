import random
import math
import sys


def prime_check(n):
    '''Function checks if provided number is prime'''
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False

    for i in range(3, int(n**0.5)+2, 2):
        if n % i == 0:
            return False
    return True


def prime_gen(choice):
    '''Function generates prime numbers with help of prime_check.
    There's two options for those numbers: manual or automatic providing.
    '''
    min_number = 2
    max_number = 10000
    products = []

    while True:
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
            if products[0] == products[1]:
                products = []
                continue
            break
    return products


def multiplicative_inverse(a, b):
    '''Function makes multiplicative inversion by using generated e and phi'''
    for lx in range(0, b):
        if (a*lx) % b == 1:
            return lx
    sys.exit(-1)


def key_gen(p, q):
    '''Function generates public and private keys using provided primes'''
    n = p * q
    phi = (p - 1) * (q - 1)

    # Generating e which will be relatively prime to phi
    while True:
        e = random.randrange(1, phi)
        if math.gcd(e, phi) == 1:
            break

    d = multiplicative_inverse(e, phi)

    return((n, e), (n, d))


def encrypt(private, plaintext):
    '''Encryption with previously generated private key'''
    n, key = private
    # Generator which converts each letter in the plaintext
    # to numbers based on the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]

    return cipher

def decrypt(public, ciphertext):
    '''Decryption with previously generated public key'''
    n, key = public
    # Generator which generate the plaintext based
    # on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]

    return ''.join(plain)


choice = input('Manual (1) or Auto (anything else): ')
if choice == '1':
    choice = 'manual'
else:
    choice = 'auto'

first, second = prime_gen(choice)
print(f'First prime:  {first}\n'
      f'Second prime: {second}')

public_key, private_key = key_gen(first, second)
print(f'--- Public key ---\n{public_key}\n'
      f'\n--- Private key ---\n{private_key}\n')

text = input("Type message: ")

enc_text = encrypt(private_key, text)
print('\n*** Encrypted message ***')
print(''.join(map(lambda x: str(x), enc_text)))
dec_text = decrypt(public_key, enc_text)
print('\n*** Decrypted message ***\n'
      f'{dec_text}')
sys.exit(0)
