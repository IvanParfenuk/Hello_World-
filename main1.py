
#
# import random
#
# f = int(random.randint(100,999))
# a = f % 10
# b = f % 100 // 10
# c = f // 100
# s = a + b + c
#
# print(a)
# print(b)
# print(c)
# print(s)




#
# numb=int(input("Введите порядковый номер пальца"))
# if numb==1:
# print("Большой")
#
# else numb==2
# print("Указательный")
# else numb==3
# print("Средний")
# else numb==4
# print("Безымянный")
# else numb==5
# print("Мизинец")







#
# a=int(input("Введите первое целое число"))
# b=int(input("Введите второе целое число"))
# c=int(input("Введите третье целое число"))
# if a>c and b>a:
#     print("Наибольшее b")
# if a<c and b<a:
#     print("Наибольшее с")
# if a>c and b<a:
#     print("Наибольшее a")




# Введите число в промежутке от 1 до 3, в правильном порядке
# a=int(input("Введите трёхзначное число:"))
# if a==312:
#     print("Лотерея выиграла)")
# elif a==123:
#     print("Лотерея проиграла(")
# elif a==231:
#     print("Лотерея проиграла(")
# elif a==321:
#     print("Лотерея проиграла(")
# elif a==213:
#     print("Лотерея проиграла(")
# elif a==132:
#     print("Лотерея проиграла(")
# else:
#     print("Нет соотвествий")



















# Записать в массив все числа в диапазоне от 1 до 500 кратные 5.
# f=[]
# for i in range(1,500):
#     if i%5==0:
#         f.append(i)
#         print(f)




# Вывести на экран все чётные значения в диапазоне от 1 до 497.
# for i in range(1,497):
#     if i%2==0:
#         print(i)


# Дан массив чисел. Если число встречается более двух раз, то добавить его в новый массив.
# from random import randint
# elements = [randint(1, 10) for _ in range(10)]
# print(elements)
# new_elements = []
# for i in elements:
#     if i in new_elements:
#         continue
#     elif elements.count(i) >= 2:
#         new_elements.append(i)
# print('Список из повторяемых чисел предыдущего списка:', new_elements)






# i = 0
# while i < 10:
#     print(i)
#     if i == 5:
#         break
#
#     i += 1

# i = 1
# result = 0
# while i <= 50:
#     result += i
#     i += 1
# print(result)


# i = 1
# while i <= 10:
#     print(i**2)
#     i += 1


# i = 1
# p= 1
# while i <= 125:
#     if i % 2 == 0:
#         p *= i
#     i += 1
# print(p)



# for i in range(3):
#     print(i)
# else:
#     print('Готово')



# i = 0
# while i < 3:
#     print(i)
#     i += 1
# else:
#     print('Готово')

#сделать так, чтобы после указанных чисел, чтобы компьютер считал в этом промежутке все отрицательные числа
# i = int(input("Введите первое число:"))
# a = int(input('Введите второе число:'))
# while i < a:
#     i += 1
#     if i == 0:
#         break
#     print(i)



# Калькулятор:
# import random
#
# f = int(input('Введите первое число:'))
# d = int(input('Введите второе число:'))
# a = (input('Введите операцию:'))
#
# if a == '/':
#     print(f/d)
#     while f > d:
#     if d == 0:
#         print('оШИБКА')
# if a == '+':
#     print(f+d)
# if a == '-':
#     print(f-d)
# if a == '*':
#     print(f*d)






# from random import randint
# elements = [randint(1, 10) for _ in range(10)]
# print(elements)
# new_elements = []
# for i in elements:
#     if i in new_elements:
#         continue
#     elif elements.count(i) >= 2:
#         new_elements.append(i)
# print('Список из повторяемых чисел предыдущего списка:', new_elements


# import random
# d = random.randint(1,10)
# a = input('Введите номер в промежутке (1,10):')
# l = random.randint(1,2)
# f = input('Введите: красный(1), чёрный(2):')
# while a == d and f == l:
#     print('Победа!')
# elif a < d and  <


# elements = [1, 3, 'a', 6, ,]
# print(elements)
#
#
#
# elements = list()
# print(elements)






# import random
# c = [random.randint(0,100) for i in range(10)]
# print(c)
#
#
# print(c[0])
# print(c[-1])
# print(c[5])
# print(c[-4])


# elements = []
# elements.append('a')
# elements.append(1)
#
# print(elements)

# вставляем 2 в список. insert(1,2) где 1 - это индекс, а 2 это нужное значение
# elements = [1, 3, 'a', 6, 'b']
# elements.insert(1,2)
# print(elements)

# замена 3 на 2. в списке 3 имеет индекс 1, поэтому elements[1]
# elements = [1, 3, 'a', 6, 'b']
# elements[1] = 2
# print(elements)

# удаление из списка определённого значения
# elements = [1, 3, 'a', 6, 'b']
# del elements[1]
# print(elements)

# удаление и списка определённого слова или выражения. Применяем remove.
# удалиться только одно а
# elements = [1, 3, 'a', 6, 'a', 'b']
# elements.remove('a')
# print(elements)



# my_list = ['hello', ' world']
# elements = [1, 3, my_list, 6, 'a', 'b']
# del elements[2][1]


# Проверяем, есть ли в списке элемент:
# elements = [1, 3, 6, 'a', 'b', 'abc', 123, 435]
# if 'abc' in elements:
#     print('Yes')





# a = [1, 3, 5]
# b = [1,5,8,9]
# print(a+b)
#
#
# d = ['h','e','l','l','o']
# e=['w','o','r','l','d']
#
# d.extend(e)
# print(d)

# для копирования используют различные способы:
# 1)
# a=['кот','слон','змея']
# b=a.copy()
# print(a,b)
# # 2)
# d=list(a)
# print(a,d)
# #3)
# import copy
# e=copy.copy(a)
# print(a,e)
#
# f=copy.deepcopy(a)
# print(a,f)
#
# # 4)
# c=a[:]
# print(a,c)





# копирование части списка с помощью срезов.
# a=['кот','слон','змея']
# b=a[2:]
# print(b)
# c=a[:2]
# print(c)
# d=a[1:2]
# print(d)
# a=[1,2,3,4,5,6,7,8]
# e=a[0:8:2]
# print(e)

# для перебора списков используют циклы for and while:
# for
# elements = [1, 2, 3, 'meow']
# for i in elements:
#     print(i)
# # while
# elements = [1, 2, 3, 'meow']
# elements_len = len(elements)
# i = 0
# while i < elements_len:
#     print(elements[i])
#     i += 1






# clear - удаляет все элементы
# a=[1,2,3]
# a.clear()
# print(a)
# # copy - копирует
# a=[1,2,3]
# b=a.copy()
# print(id(a), id(b), a, b)
# # count - количество вхождений
# elements = ['one','two','three','one','two','one']
# print(elements.count('one'))
# # index -
# elements = ['one','two','three','one','two','one']
# print(elements.index('three'))




# pop
# elements = [1,'meow',3,'meow']
# # удаляем элемент с индексом 1
# elements.pop(1)
# 'meow'
# print(elements)
#
# # удаляем первый элемент списка
# elements.pop()
# print(elements)
#
# # удаляем последний элемент списка
# elements.pop(-1)
# print(elements)
#
# # reverse
# a=[1,2,3]
# a.reverse()
# print(a)




# sort(по возрастянию)
# elements=[3,19,0,3,102,3,1]
# elements.sort()
# print(elements)
#
# # sort (по убыванию)
# elements=[3,19,0,3,102,3,1]
# elements.sort(reverse=True)
# print(elements)
#
#
# вложенные списки
# elements=[['яблоки', 50],['апельсины',190],['груши', 100]]
# print(elements[0])
# print(elements[1][0])
#
#
# from random import randint
# elements=[randint(1,20) for i in range(10)]
# elements_line=()
# print(elements)
# elements.reverse()
# print(elements)
#
#
# a=my_list.index
# my_list=[1,4,5,3,7,15,20,21,25]
# if 20 in my_list:
#      print('Есть число 20')
#      print(my_list.index(20))
# my_list = 200
# print(my_list)
#
#
# a = ['one', 'two', 'three', 'one', 'two', 'one']
# printfor



# a=input('Введите семизначное число:')
# b=('Четные:')
# c=('Нечётные:')
# d=a%10
# if d % 2 ==0:
#     print(b)
# e
# a.index([5]) % 2






# a=('Введите текст:')
# b=('Гласных:')
# c=('Согласных:')
# if "а"in a:
#     print(b)


