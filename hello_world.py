# 1
# num = input('Введите семизначное число:')
# col =[]
# life = []
# bs = 0
# cl = 0
# groza = 1
#
# # for i in num:
#
# for i in range (len(col)):
#     elements = int(col[i])
#     life.append(elements)
#     print(life)
# for i in life:
#     if i % 2 == 0:
#         bs += 1
#         print('bs=', bs)
#     elif i % 2 != 0:
#         cl += 1
#         print('cl=', cl)
#     if bs > cl:
# for i in life:
#     groza*=i
#     print(groza)
# elif bs < cl:
# f = life[0]*life[2]*life[5]
# print(f)
# else:
# print('Неправильное число!!!')













# 2
# num = input('Введите текст:')
# col1=[]
# var2=[]
# col = 0
# var = 0
# for i in num:
#     if i == 'а' or i == 'о'\
#             or i == 'э' or i == 'е'\
#             or i == 'и' or i =='ы' \
#             or i == 'у' or i == 'ё'\
#             or i == 'ю' or i == 'я':
#         col1.append(i)
#         print(i)
#         col += 1
#         print('col=', col)
#     elif col1 < var2:
#             print('Согласных больше:',var)
#
#
#     elif i =='б' or i == 'в' \
#         or i == 'г' or i == 'д' \
#            or i == 'ж' or i == 'з' \
#            or i == 'й' or i == 'к' \
#            or i == 'л' or i == 'м' \
#            or i == 'н' or i == 'п' \
#            or i == 'р' or i == 'с' \
#            or i == 'т' or i == 'ф' \
#            or i == 'х' or i == 'ц' \
#            or i == 'ч' or i == 'ш' \
#            or i == 'щ':
#         var2.append(i)
#         print(i)
#         var += 1
#         print('var=', var)
#     else:
#         print('Неотносится ни к гласным, ни к согласным',i)


# Задача из контрольной 3
# from random import randint
# num1 = randint(1,20)
# num = input('Введите два числа от 1 до 20:')
# var = 0
# rand = 0
# list = []
# for i in num1:
#     if num > i:
#         var += 1
#     else:
#         rand += 1








# from random import randint
# list = randint(1,100)
# num = input()
# print(list)
# while i < 10:
#     if













# stroka = input('Введите слово:')
# cht = 0
# los = 0
# summ = []
# frunk = []
# gold = []
# pro = []
# for i in stroka:
#     if i in "aeoiu":
#         summ.append(i)
#         cht += 1
#         print(i)
#     else:
#         frunk.append(i)
#         print(i)
# if i.isupper():
#     gold.append(i)
#     los += 1
# else:
#     pro.append(i)

# arr = ('asd', 'asdfb', 'bcd', 'a')
#
#
#
# print(min(arr, key=len))
# print(max(arr, key=len)
#



# Задача 1 из урока Кортежи
# from random import randint
# elements = tuple(randint(1,1000) for _ in range(10))
# print(elements)
# print('min', min(elements), 'max', max(elements))










# Задача 2 из урока кортежи
# from random import randint
# elements = tuple(randint(0,5) for _ in range(10))
# new_elements = tuple(randint(-5,0) for _ in range(10))
# print(elements)
# print(new_elements)
# new_elements1 = elements + new_elements
# print(new_elements1)
# print(new_elements1.count(0))






# 2
# A = (13, 5, 43, 49, 67, 32, 12, 98, 6, 10, 34, 20, 55, 68, 14, 60, 14)
# B = (53, 21, 4, 23, 76, 3, 43, 12, 54, 342, 21)
# pro = sum(A)
# print('Сумма кортежа А:',pro)
# new_pro = sum(B)
# print('Сумма кортежа В:', new_pro)
# if pro > new_pro:
#     print('Сумма больше в кортеже - A')
# else:
#     print('Сумма больше в кортеже - B')
# print('min в кортеже А:', min(A))
# print('min в кортеже В:', min(B))







# d = dict.fromkeys(['a','b'])
# d_2 = dict.fromkeys(['a','b'],100)
# print(d, '\n', d_2)




# d = {a: a ** 2 for a in range(7)}
# print(d)



# d = {1:2,2:4,3:9}
# d[4]=4**2
# print(d[1])
# print(d)

# Словарь
# Months = {1:'Jan', 2:'Feb', 3:'Mar',  4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
# count = len(Months)
# print(count)

# Словарь
# Salary = {'Director': 120800.0,
#           'Secretary': 101150.25,
#           'Locksmith': 188200.00}
# print(Salary)
#
# # Удалить элемент по ключу 'Secretary' с проверкой
# key = 'Secretary'
# if key in Salary:
#     del Salary['Secretary']
#     print(Salary)
#
# # Попытка удалить несуществующий ключ
# # если ключа нету, то исключить KeyError не генерируется
# key2 = 5
# if key2 in Salary:
#     del Salary[key2]






# Position = {'Manager': {'Director',
#                         'Deputy Director'},
#             'Teacher': {'Specialist',
#                         'Manthodist',
#                         'Senior Lecturer'},
#             'Staff': {'Cleaner',
#                       'Porter',
#                       'Watchman'}}
#
# count1 = len(Position)
# count2 = len(Position['Manager'])
# count3 = len(Position['Staff'])
#
# print(Position,'len:', count1,'\n',
#       Position['Manager'],'len:', count2,'\n',
#       Position['Staff'],'len:', count3,'\n')








# Операция not in - определение отсутсвия ключа в словаре
# Формирование словаря слов их числовым эквивалентом

# 1. Сформировать пустой словарь
# Words = dict() # Words = {}
# 2. Ввести количество слов в словаре
# count = int(input('Количество слов в словаре:'))
# 3. Цикл добавления слов
# i = 0
# while i<count:
#     print('Ввод слов')
#     wrd = str(input('Слово:'))
#     value = int(input('Значение:'))
# # Если ключа wrd нет в словаре, то добавить пару [wrd:value]
# if wrd not in Words:
#     Words[wrd] = value
# i=i+1
# Вывести сформированный словарь










# Numbers = dict(zip([1,2,3],['One','Two','Three']))
# print(Numbers)



# Months = {1:'Jan', 2:'Feb', 3:'Mar',
#           4:'Apr', 5:'May', 6:'Jun',
#           7:'Jul', 8:'Aug', 9:'Sep',
#           10:'Oct', 11:'Nov', 12:'Dec'}
#
# for mn in Months:
#     print(mn, ': ', Months[mn])










# person = {'name':'Алексей', 'age':'21', 'city':'Минск'}
# print(person['age'])





# Car = {'BMW':[ 'x5','320d','i8'],
#        'Tesla':['Model X', 'Model S', 'Model 3']}
# print(Car['BMW'][0],Car['BMW'][2], '\n',
#       Car['Tesla'][0],Car['Tesla'][2])







# d1 = {'a':100,'b':200,'c':300}
# d2 = {'a':300,'b':200,'d':400}
#
# print(d1['b']==d2['b'])


#                 МНОЖЕСТВА
# string_set = {'Nicholas','Nichelle','John','Mercy'}
# print(string_set)


# mixed_set = {2.0,'Nicholas',(1,2,3)}
# print(mixed_set)



# num_set = set([1,2,3,1,2])
# print(num_set)



# num_set = {1,2,3,1,2}
# print(num_set)



# x = set()
# print(type(x))



# months={'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'}
# for m in months:
#     print(m)



# months={'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'}
# print('May' in months)


# months=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# months.add('Feb')
# print(months)


# Удаление элемента из множества с помощью discard
# num_set={1,2,3,4,5,6}
# num_set.discard(3)
# print(num_set)



#  Удаление элемента из множества с помощью REMOVE
# num_set={1,2,3,4,5,6}
# num_set.remove(3)
# print(num_set)

# Удаление элемента из множества с помощью POP
# num_set={1,2,3,4,5,6}
# num_set.pop()
# print(num_set)

# Удаляет все элементы из множества (clear)
# num_set={1,2,3,4,5,6}
# num_set.clear()
# print(num_set)

# Метод union нужен для объединения множеств
# months_a={'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'}
# months_b={'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'}
# all_months=months_a.union(months_b)
# print(all_months)


# Объединение нескольких множеств с помощью union
# x={1,2,3}
# y={4,5,6}
# z={7,4,9}
# output=x.union(y,z)
# print(output)


# Объединение при помощи |
# months_a={'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'}
# months_b={'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'}
# print(months_a | months_b)

# Объединение при помощи | нескольких множеств
# x={1,2,3}
# y={4,5,6}
# z={7,4,9}
# print(x|y|z)


# Для поиска пересечений во множествах, при помощи & (shift + 7)
# x={1,2,3,4}
# y={4,3,6}
# print(x & y)


# Находим разницу между множествами
# A = {1,2,3}
# B = {4,3,6}
#
# print(A-B)
# print(B-A)


# string_set = {'Nicholas','Nichelle','John','Mercy'}
# x = string_set.copy()
#
# print(x)

# При помощи метода  isdisjoint ищем перечения, если их нету, то будет True, если они есть, то будет False
# names_a = {'Nicholas','Nichelle','John','Mercy'}
# names_b = {'Jeff','Bosco','Teddy','Milly'}
# x = names_a.isdisjoint(names_b)
# print(x)

# С помощью метода len ищем длину
# names_a = {'Nicholas','Nichelle','John','Mercy'}
# print(len(names_a))


# Тип данных frozenset
# ny_set=frozenset([1,2,3,-10,40])
# print(type(ny_set))



# 1 Создать множество
# x = set(1,3,4,5,8,2)

# 2 Создать неизменяемое множество
# x1 = fronzenset([9,10,6,11,12,7])

# 3 Объединение множеств
# print(x|x1)


#    ТИП ДАННЫХ
# try:
#     k = 1 / 0
# except ArithmeticError:
#     k = 0
# print(k)


# my_dict = {'a':1,'b':2,'c':3}
# try:
#     value = my_dict['d']
# except KeyError:
#     print('Ключа не существует!')


# my_list = [1,2,3,4,5]
# try:
#     my_list[6]
# except IndexError:
#     print('Индекса не существует!')


# Стандартный способ, для ловли исключений !!!
# my_dict = {'a':1,'b':2,'c':3}
# try:
#     value = my_dict['d']
# except IndexError:
#     print('Такого индекса не существует!')
# except KeyError:
#     print('Этого ключа нет в  словаре!')
# except:
#     print('Произошла другая ошибка!')






# Универсальный способ, но лучше стандартный
# my_dict = {'a':1,'b':2,'c':3}
# try:
#     value = my_dict['d']
# except (IndexError, KeyError):
#     print('Произошла ошибка IndexError или KeyError!')



# my_dict = {'a':1,'b':2,'c':3}
# try:
#     value = my_dict['d']
# except KeyError:
#     print('Произошла ошибка KeyError!')
# finally:
#     print('Оператор finally выполнен!')




# my_dict = {'a':1,'b':2,'c':3}
# try:
#     value = my_dict['d']
# except KeyError:
#     print('Произошла ошибка KeyError!')
# else:
#     print('Ошибок не произошло!')
# finally:
#     print('Оператор finally выполнен!')



# n = input('Введите строку:')
# n_1 = n.replace('','')
# if type(n_1) is int:
# print(int(n_1[0])/int(n_1[1]))

    # if l =='+':
    #     print(n+n_1)
    # elif l == '-':
    #     print(n-n_1)
    # elif l == '*':
    #     print(n*n_1)
    # elif l == '/':
    #     if n_1 != 0:
    #         print(n / n_1)
    #     try:
    #         if n_1 == 0 and n / n_1:
    #             print('Ошибка')
    #     except ZeroDivisionError:
    #         print('Произошла ошибка ZeroDivisionError!')
    #     finally:
    #         print('Оператор finally выполнен!')




# фАЙЛЫ

# f = open('example.txt','r')
# # fp = open('C:/xyz.txt','r')
# try:
#     print(*f)
# finally:
#     f.close()


# with open('example.txt') as f:
#     print(*f)

# Интерпретатор прочитает 7 символов файла и если снова использовать функцию read(), то чтение начнется с 8-го символа.
# f = open('example.txt','r')
# print(f.read(7))

# Функция readline помогает прочитать некоторые строки, в данном случае 1 и 2
# x = open('example.txt','r')
# print(x.readline())
# print(x.readline())


# Функция readlines помогает прочитать все строки
# x = open('example.txt','r')
# print(x.readlines())


# Предположим, файла xyz.txt не существует. Он будет создан при попытке открыть его в режиме чтения.
# f = open('xyz.txt', 'w')
# f.write('Hello \n World')
# f.close()




# import os
#
# print('Текущая деректория:', os.getcwd())
# os.chdir('klin')
# print('Текущая директория изменилась на klin:', os.getcwd())



# import os
# os.chdir('klin')
# os.chdir('..')
# os.makedirs('nested1/nested2/nested3')



# import os
# print('Текущая директория изменилась на klin:', os.getcwd())
# os.remove('klin/example.txt')


# import os
# # удалить папку, можно только когда в ней нету файлов.
# os.rmdir('klin')

# import os
# # удалить вложенные папки
# os.removedirs('nested1/nested2/nested3')



# Практика
# with open('best.txt') as f:
#     x = f.readlines()
#     print(x)
# for i in x:
#     i = i.replace('_',' ')
#     l = i.split(' ')
# print(l)
# klin = 0
# for i in l:
#     if i.isdigit():
#         i = int(i)
#         klin += i
# print(klin)









