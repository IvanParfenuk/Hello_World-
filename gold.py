# # Задание номер 2 (кортеж) дз
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


# Задание номер 1 (кортеж) дз
# los = (1, 2, 3, 4, 5, 6, 7)
# news = []
# for i in los:
#     news.append(i)
# print(news)
# print(",".join(news))


# f = open('abc.txt')
# suma = 0
# for i in f:
#     suma += 1
#     print(i, len(i), 'симв.')
# print(suma, 'стр.')
# f.close()


# ФУНКЦИИ

# def a_function():
#     print('You just created a function!')
#
#
# a_function()


# def empty_function():
#     pass


# pro = [1,5,7,24,18]
# def line_sit():
#     print(sum(pro))
# line_sit()


# def add(a,b):
#     return a + b
# print(add(1,2))


# def add(a,b):
#     return a + b
# print(add(a=2, b=3))
#
# total = add(b=4, a=5)
# print(total)


# def keyword_function(a=1, b=2):
#     return a + b
# print(keyword_function(b=4, a=5))
# print(keyword_function())


# def keyword_function(a, b=2, c=3):
#     return a + b + c
# # keyword_function(b=4, c=5)
# print(keyword_function(1, b=4, c=5))
# print(keyword_function(1))


# def many(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# many(1,2,3, name ='Mike', job = 'programmer')


# def dlin_a():
#     global a
#     a=1
#     b=2
#     return a+b
#
# def dlin_b():
#     c=3
#     return a + c
#
# print(dlin_a())
# print(dlin_b())


# def func1(a,b):
#     def inner_func(x):
#         return x*x*x
#     return inner_func(a) + inner_func(b)
# print(func1(4,5))


# def sum(a,b): return a+b
# print(sum(1,5))


# Задача 3, а в тетради 2
# def is_year_leap(a):
#     return (a%4==0) and (a%100!=0)
# print(is_year_leap(int(input('Введите год:'))))


# Задача 4, а в тетради 3
# def season(a):
#     if a in (1,2,12):
#         return 'зима'
#     elif a in (3,4,5):
#         return 'весна'
#     elif a in (6,7,8):
#         return 'лето'
#     elif a in (9,10,11):
#         return 'осень'
#     else:
#         return 'Такого нет'
# print(season(int(input('Введите месяц:'))))

# Анономная функция: лямбда
# power = lambda x=1, y=2: x ** y
# square=power
# print(square(5))


# def mul(a):
#     def helper(b):
#         return a * b
#     return helper
# print(mul(3)(2))


# def mul(a):
#     def helper(b):
#         return a * b
#     return helper
# three_mul = mul(3)
#
# print(three_mul(5))


# Декоратор функции
# def first_test():
#     print('Test function 1')
#
# def second_test():
#     print('Test function 2')
#
# def simple_decore(fn):
#     def wrapper():
#         print('Start function')
#         fn()
#         print('Stop function')
#     return wrapper
#
# first_test_wrapped = simple_decore(first_test())
# second_test_wrapped = simple_decore(second_test())
# first_test_wrapped()
# second_test_wrapped()


# Другой способ реализовать данную идею
# def first_test():
#     print('Test function 1')
#
# def second_test():
#     print('Test function 2')
#
# def simple_decore(fn):
#     def wrapper():
#         print('Start function')
#         fn()
#         print('Stop function')
#     return wrapper
#
# @simple_decore
# def first_test():
#     print('Test function 1')
#
# first_test()


# Передаём аргументы в функцию с помощью декоратора
# def param_transfer(fn):
#     def wrapper(arg):
#
#     return wrapper
#
# @param_transfer
# def print_sqrt(num):
#     print(num ** 0.5)
#
# print_sqrt(4)


# Задание 1

# from random import random
# N = 10
#
# def func(arr,mn,mx):
#     for i in range(N):
#         arr[i] = int(random() * (mx-mn+1)) + mn
#
# arr = [0] * N
# start = int(input("Введите начало диапазона чисел: "))
# finish = int(input("Введите конец диапазона чисел: "))
# func(arr, start, finish)
# print(arr)


# ООП (классы)
# class Car:
#     color = 'Grey'
#
#     def turn_on(self):
#         pass
#     def ride(self):
#         pass
# car_object = Car()
# print(dir(Car))


# class Car:
#     # Статические поля (переменные класса). Статическиет, т.е. по умолчанию
#     # Динамические, те которые мы добавляем
#     # self -  по умолчанию
#     default_color = 'Grey'
#     default_weight = 5000
#
#     def __init__(self, color, model):
#         # Динамические поля (переменные объекта)
#         self.color = color
#         self.model = model
#
#     def turn_on(self):
#         pass


# class Example:
#     stat_color = 'Grey'
#     stat_model = 'X5'
#
#     def __init__(self, color, type):
#         self.color = color
#         self. type = type
#
#     def turn_on(self):
#
#
#
# car_obj =
# print()

#     def ride(self):
#         pass
# car_object = Car()
# print(dir(Car))


#
# @classmethod
# def toy_phone(cls, color):
#     toy_phone = cls(color, 'ToyPhone')
#     return toy_phone
# Phone.toy_phone('Red')
# print(Phone.toy_phone('Red').model)
#
#
#


# Задание 1
# class Human:
#     default_name = 'Roma'
#     default_age = 19
#
#     def __init__(self, name=default_name, age=default_age):
#         self.name = name
#         self.age = age
#         self.__money = 100
#         self.__house = '1337'
#
#     def info(self):
#         print(self.name, self.age, self.__house,self.__money)
#
#     def earn_money(self):
#         self.__money += 20
#
#     @staticmethod
#     def default_info():
#         print(Human.default_name, Human.default_age)
#
#
# Human.default_info()
# human_var = Human()
# human_var.info()
# human_var.earn_money()
# human_var.info()


# class Phone:
#
#      def __init__(self):
#          self.is_on = False
#
#      def turn_on(self):
#          self.is_on = True
#
#      def call(self):
#          if self.is_on:
#              print('Making call...')
#
# class MobilePhone(Phone):
#
#      def __init__(self):
#         super().__init__()
#         self.battery = 0
#
#      def charge(self, num):
#         self.battery = num
#         print(f'Charging battery up to ... {self.battery}%')
#
# my_mobile_phone = MobilePhone()
# print(dir(my_mobile_phone))


# b = str(input('Введите цифру: '))
#
# def schet(n):
#     try:
#         n = int(n) + int(n * 2) + int(n * 3)
#         return n
#     except ValueError:
#         print('Ввели не тот символ')
#
# k = schet(b)
# print(k)




# from random import randint
#
# element = [randint(1, 10) for _ in range(10)]
# print(element)
#
# def ariphmetic(a):
#     print(sum(a) / 10)
#
# ariphmetic(element)









# Вы также можете использовать функцию
a = 'hello'
cursor.execute('''SELECT * FROM tab_1 WHERE col_1='hello' ''')
conn.commit()
k = cursor.fetchall()
print(k)

#
cursor.execute('''SELECT * FROM tab_1 ORDER BY col_3''')
conn.commit()
k = cursor.fetchall()
print(k)

#
cursor.execute('''SELECT * FROM tab_1 WHERE col_3 LIKE '7%' ''')
conn.commit()
k = cursor.fetchall()
print(k)







