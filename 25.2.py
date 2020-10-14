import string
import random

loLetters = []
upLetters = []
digits = []
for i in string.ascii_lowercase:
    if i != 'l' and i != 'o':
        loLetters.append(i)
        random.shuffle(loLetters)
for j in string.digits:
    if j != "1" and j != "0":
        digits.append(j)
        random.shuffle(digits)
for i in string.ascii_uppercase:
    if i != 'I' and i != 'O':
        upLetters.append(i)
        random.shuffle(upLetters)
letters = loLetters + upLetters + digits
random.shuffle(letters)


def generate_password(m):
    a = [random.choice(loLetters), random.choice(upLetters), random.choice(digits)]
    while len(a) != m:
        letter = str(random.choice(letters))
        if letter not in a:
            a.append(letter)
    random.shuffle(a)
    a = "".join(a)
    return a


def main(n, m):
    passwords = []
    while len(passwords) != n:
        password = generate_password(m)
        if password not in passwords:
            passwords.append(password)
    return passwords


print('Случайный пароль из 7 символов:', generate_password(7))
print('10 случайных паролей длиной 15 символов:')
print(*main(10, 15), sep='\n')
