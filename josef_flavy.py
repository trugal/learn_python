"""n человек, пронумерованных числами от 1 до n, стоят в кругу. Они начинают считаться, каждый k-й по счету
человек выбывает из круга, после чего счет продолжается со следующего за ним человека.
Напишите программу, определяющую номер человека, который останется в кругу последним."""
n = int(input())
list = [i for i in range(1, n+1)]
print(list)
k = int(input())
current = 0
count = 0
while len(list)>1:
    for _ in range(k-1):
        list += list.pop(0)
    del list[0]

print(list)

