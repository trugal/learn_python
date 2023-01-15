# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import random


def is_valid(string, maxim):
    """Проверяется является ли введенная строка целым числом в диапазоне от 1 до числа maxim включительно"""
    try:
        num = int(string)
        if num in range(1, maxim + 1):
            return True
        else:
            return False
    except ValueError:
        return False

def one_try():
    print('Игра началась!')
    right = int(input('Введите максимально возможное число для угадывания: '))
    n = random.randint(1, right)
    counter = 1
    while True:
        numstr = input(f'Введите целое число в диапазоне от 1 до {right}: ')
        if is_valid(numstr, right):
            number = int(numstr)
            if number == n:
                print(f'Вы угадали за {counter} попыток, поздравляем!')
                counter = 1

                break
            else:
                print('Ваше число меньше загаданного, попробуйте еще разок' if number < n else
                      'Ваше число больше загаданного, попробуйте еще разок')
                counter += 1
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue





print("Добро пожаловать в числовую угадайку")
flag = True
all_tries_count = 1
while flag:
    print('Игра номер', all_tries_count)
    one_try()
    continue_play = input('Для продолжения введите YES, в прротивном случае игра прервется - ')
    if continue_play == 'YES':
        all_tries_count += 1
        continue
    else:
        print('Спасибо за игру!')
        break





