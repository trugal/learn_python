
print('Добро пожаловать')
str = input()
alphabetlow = 'abcdefghijklmnopqrstuvwxyz'
alphabetup = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
list = str.split()
for j in range(len(list)):
    shift = 0
    newword = ''
    for c in list[j]:
        if c.isalpha():
            shift += 1
    for i in range(len(list[j])):
        if list[j][i].isupper():
            ind = alphabetup.find(list[j][i])
            newword += alphabetup[(ind + shift) % 26]
        elif list[j][i].islower():
            ind = alphabetlow.find(list[j][i])
            newword += alphabetlow[(ind + shift) % 26]
        else:
            newword += list[j][i]
            continue
    list[j] = newword
print(" ".join(list))




