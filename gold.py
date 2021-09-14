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


f = open('abc.txt')
suma = 0
for i in f:
    suma += 1
    print(i, len(i), 'симв.')
print(suma, 'стр.')
f.close()





