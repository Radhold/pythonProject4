import string
import random

letters = []
for i in string.ascii_letters:
    if i != "l" and i != "I" and i != "o" and i != "O":
        letters.append(i)
        random.shuffle(letters)
for j in string.digits:
    if j != "1" and j != "0":
        letters.append(j)
        random.shuffle(letters)


def generate_password(m):
    a = []
    while len(a) != m:
        letter = str(random.choice(letters))
        if letter not in a:
            a.append(letter)
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
