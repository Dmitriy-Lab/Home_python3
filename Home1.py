# Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи

fibo = open('text.txt', 'w', encoding='utf-8')
n = int(input("Введите число N: "))
fibo.write('1 ')
a1 = 0
a2 = 1

for i in range(2, n + 1):
    sum = a1 + a2
    a1 = a2
    a2 = sum
    str_a2 = str(a2)
    fibo.write(str_a2 + ' ')

fibo.close()