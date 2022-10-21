# В файле находятся названия фруктов. 
# Выведите все фрукты, названия которых начинаются на заданную букву

n = (input("Введите букву: ")).upper()
frukt = open('frukt.txt', 'r', encoding='utf-8')
read = frukt.readlines()
frukt.close()

only_one = []
for i in read:
    if i.startswith(n):
        only_one.append(i)
print(only_one)