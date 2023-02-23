# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

num_n = int(input('Кооличество элементов 1 множества: '))
num_m = int(input('Кооличество элементов 2 множества: '))
# list_1 = list()
# for i in range(num_n):
#     n = int(input())
#     list_1.append(n)
# print('Введите элементы множества')
# list_2 = list()
# for i in range(num_m):
#     m = int(input())
#     list_2.append(m)
# print(list_1)
# print(list_2)
# one = set(list_1)
# two = set(list_2)

print('Введите элементы множества')
one = set()
for i in range(num_n):
    n = int(input())
    one.add(n)
print('Введите элементы множества')
two = set()
for i in range(num_m):
    m = int(input())
    two.add(m)
print(f'Множество 1= {one}')
print(f'Множество 2= {two}')
b = one.intersection(two)
print(f'Пересечение= {b}')
