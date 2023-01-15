
import random
import sys


def generate_password(length, chars):
    result = ''
    for _ in range(length):
        result += chars[random.randint(0, len(chars)-1)]
    return result


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
difficult_symbols = 'il1Lo0O'
chars = []
pass_num = int(input('Введите необходимое количество паролей: '))
pass_len = int(input('Какой длины должны быть пароли: '))
if input('Нужно ли испсользовать цифры в пароле? введите yes если да: ').lower() == 'yes':
    chars.extend(digits)
if input('Нужно ли испсользовать маленькие буквы в пароле? введите yes если да: ').lower() == 'yes':
    chars.extend(lowercase_letters)
if input('Нужно ли испсользовать большие буквы в пароле? введите yes если да: ').lower() == 'yes':
    chars.extend(uppercase_letters)
if input('Нужно ли испсользовать спецсимволы в пароле? введите yes если да: ').lower() == 'yes':
    chars.extend(punctuation)
if input('Нужно ли убрать неоднозначные символы из пароля? введите yes если да: ').lower() == 'yes':
    for c in difficult_symbols:
        try:
            chars.remove(c)
        except ValueError:
            continue
if len(chars) == 0:
    print('Пароль из пустых симоволов не может существовать.')
    sys.exit()
else:
    print(chars)
    for _ in range(pass_num):
        print(generate_password(pass_len, chars))

