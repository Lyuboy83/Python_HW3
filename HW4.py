# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

# from random import randint 
# n = int(input("Введите количество первого множества: "))
# m = int(input("Введите количество второго множества: "))
# list1 = [(randint(0, 10)) for i in range(n)]
# list2 = [(randint(0, 10)) for i in range(m)]
# list3 = []
# # for i in range(n):
# #     list2.append(randint(0, 10))  
  
    
# # for i in range(m):
# #     list2.append(randint(0, 10))
# print(list1) 
# print(list2)
# for i in list1:
#     for j in list2:
#         if i == j:
#                 list3.append(i)

# list3 = set(list3)
# list3 = sorted(list3)
# print(list3)  

# Альтернативное решение Олег


# from random import randint 
# n = int(input("Введите количество первого множества: "))
# m = int(input("Введите количество второго множества: "))
# list1 = [(randint(0, 10)) for i in range(n)]
# list2 = [(randint(0, 10)) for i in range(m)]
# list3 = []
# # for i in range(n):
# #     list2.append(randint(0, 10))  
  
    
# # for i in range(m):
# #     list2.append(randint(0, 10))
# print(list1) 
# print(list2)
# new_nums = []
# for i in list1:
#     if i in list2 and not i in new_nums:
#         new_nums.append(i) 

# print(*sorted(new_nums))       


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

# list = [1,2,3,4,5,6,7]
# # sum1 = list[0]+ list[1] + list[-1]
# # sum2 = list[0] + list[-1] + list[-2]
# # summ = list[0] + list[1] + list[2]

# a = 0
# for i in range(1, len(list)-1):
#     sum3 = list[i] + list[i-1] + list[i+1]
#     if sum3 > summ:
#         summ = sum3
# a = max(sum1, sum2, summ)
# print(a)

# list = [1,2,3,4,5,6,7]
# sum1 = max(list[0]+ list[1] + list[-1],
#            list[0] + list[-1] + list[-2])

# for i in range(1, len(list)-1):
#     sum2 = list[i] + list[i-1] + list[i+1]
#     if sum2 > sum1:
#         sum1 = sum2

# print(sum1)

# Олег


# import random
# n = int(input('Введите колличество кустов: '))

# garden = [random.randint(1, 6) for i in range(n)]
# print(*garden)

# max_bushes  = garden[0] + garden[1] + garden[2]

# for i in range (len(garden)):
#     following_bushes = garden[1] + garden[2] + garden[3]
#     if following_bushes > max_bushes:
#         max_bushes = following_bushes 
#     temp = garden.pop(0)
#     garden.append(temp)

# print(f"Максимальное число ягод за один заход = {max_bushes}")