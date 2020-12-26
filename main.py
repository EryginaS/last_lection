# l1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 7, 7, 7, 10, 10, 10, 10, 8, 8, 8, 8, 8]
# s1 = set(l1)  # уникальные элементы
# l2 = list(s1)
# d1 = {}  # словарь 1
# for i in range(1, len(l2)+1):
#     d1[i] = l2[i-1]
# print(d1)
# d1 = {i+1: l2[i] for i in range(len(l2))}
# print(d1)
# d2 = {}
# for i in l2:
#     d2[i] = l1.count(i)
# print(d2)
# dd2 = {i: l1.count(i) for i in l2}
# print(dd2)
# def mul(a, b):
#     return a * b
#
#
# print(mul(2, 3))
# print(mul(7, 3))
#
#
# def ost(a):
#     return a % 3
#
#
# def about_string(string):
#     l = len(string)
#     s1 = string.upper()
#     s2 = string.lower()
#     return l, s1, s2
#
#
# print(about_string('kkkkkkk'))
#
#
# def con(d1, d2, d3):
#     d1.update(d2)
#     d1.update(d3)
#     return d1
#
#
# x = {'a': 1, 'b': 2}
# y = {'b': 10, 'c': 11}
# z = {2: 'r'}
# print(con(x, y, z))

#
# def am(name="No name", age=10):
#     name = name.upper()
#     age = age + 5
#     return name, age
#
# print(am(age = 12, name = 'Sveta' ))
#
# def sumer(*args):
#     print(args[0])
#     sum1 = sum(args)
#     return sum1
# print(sumer(2,3,3,4,5,6))
#
# def am(*args,**kwargs):
#
#     print(args,kwargs)
#     pass
# am(2,3,4,5,6,'dhge',name = "sveta",age=22, street = 'Соловьева')
import math
print(math.cos(1))