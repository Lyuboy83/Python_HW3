# my_list = [1, 1, 2, 0, -1, 3, 4, 4, 3, -3, 0, 10, 11, 11]
# unique = []
# for i in my_list:
#     if i not in unique:
#         unique.append(i)
# print(my_list)
# print(len(unique))






# 21:42
# Вадим Кардаполов
# # for i in a:
# #     if a.count(i) > 1 :
# #         for j in range(a.count(i)-1):
# #             a.remove(i)
# # print(len(a))
# # print(a)





# 21:44
# Андрей Дубровский
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# k = 7
# for i in range(k):
#     my_list.insert(0, my_list[-1])
#     my_list.pop(-1)
# print(my_list)

# new_list = []
# for i in my_list:
#     if i - k > 0:
#         new_list.append(i - k)
#     else:
#         new_list.append(i - k + len(my_list))
# print(new_list)



# Артур Балухтин
# Администратор
# lst = [1, 2, 3, 4, 5]
# k = 2
# for i in range(k):
#     lst.insert(0,lst.pop())
# print(lst)

# lst = [1, 2, 3, 4, 5]
# a1 = lst[-k:]
# a2 = lst[:-k]
# print(a1+a2)


# Артур Балухтин
# Администратор
# list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
#           {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]

# set_n = set()

# for dct in list_1:
#    set_n.add(str(*dct.values()).strip())
   
# print(set_n)

# my_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
#            {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
# print(set().union(*(d.values() for d in my_list)))

#Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером)
# list_1 = [0, -1, 5, 2, 3]
# count = 0
# for i in range(1,len(list_1)):
#     if list_1[i]>list_1[i-1]:
#         count+=1
#
# print(count)







# s = int(input())
# p = int(input())

# #x+y=s->
# #x*y=p
# flag = False
# for x in range(1000):
#     for y in range(1000):
#         if (x+y) == s and x*y == p:
#             print(x,y)
#             flag = True
#             break
#     if flag:
#         break


# n = int(input())
# #
# # stepen = 0
# # while 2**stepen<n:
# #     print(2**stepen)
# #     stepen += 1

