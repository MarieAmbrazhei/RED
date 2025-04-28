# 1
# Продвинутый sum.
# Встроенная функция sum() в python вызывает ошибку, если один из элементов последовательности не является числом, например sum([1, 2, ‘A’]).
# Напишите функцию sum_ignore_non_numbers(), которая имеет один параметр items (список или кортеж).
# Функция должна вернуть сумму всех чисел (int, float) в переданной последовательности. При этом все нечисловые значения должны игнорироваться.
# Если чисел нет, то функция должна вернуть 0.
# Если вызвать функцию со списком [1, 2, 'Hey', None, 4.3], то она должна вернуть 7.3


# def sum_ignore_non_numbers(items):
# return [sum(num for num in items if isinstance(num, (int, float)))]
# count = 0
# for num in items:
#     if isinstance(num, (int, float)):
#         count += num
# return count


# print(sum_ignore_non_numbers(['A']))


# 2
# Треугольник.
# Треугольник возможен, если сумма любых двух его сторон больше длины третьей стороны.
# Напишите функцию is_triangle(), которая имеет 3 параметра - длины сторон треугольника.
# Функция должна возвращать True, если треугольник с переданными сторонами может существовать, и False в противном случае.
# Для is_triangle(2, 4, 9) правильный ответ - False, для is_triangle(3, 4, 5) - True.


# def is_triangle(a, b, c):
# if a + b > c and a + c > b and b + c > a:
#     return True
# else:
#     return False
# return a + b > c and a + c > b and b + c > a


# print(is_triangle(3, 4, 5))


# Среднее значение.
# Напишите функцию average(), которая принимает произвольное количество позиционных аргументов. (Можно передать любое число аргументов).
# Функция должна посчитать среднее арифметическое всех переданных чисел. (Представим, что в функцию передаются только числа).
# Если не передать ни одного аргумента, то функция должна вернуть 0.
# Такой вызова функции average(1, 2, 3, 4, 5, 6, 7, 8) должен вернуть 4.5


# def average(*args):
# count = 0
# len_ls = 0
# for num in args:
#     if isinstance(num, (int, float)):
#         count += num
#         len_ls += 1
# return count/len_ls
# ********
# ls = []
# for num in args:
#     if isinstance(num, (int, float)):
#         ls.append(num)
#
# if not ls:
#     return 0
# return sum(ls) / len(ls)
#     my_ls = [num for num in args if isinstance(num, (int, float))]
#     if not my_ls:
#         return 0
#     return sum(my_ls) / len(my_ls)
#
#
# print(average(1, 2, 3))


# 4
# Общие строки.
# Напишите функцию common_strings(), которая имеет 3 параметра: list1, list2 и ingore_case=True (значение по умолчанию).
# Функция должна вернуть новых список из тех значений, которые встречаются в обоих списках. При этом, если ignore_case равен True, то функция должна игнорировать регистр и считать строки “string” и “STRING” одинаковыми.  В противном случае функция должна учитывать регистр символов и считать такие строки разными.
# Все строки в результирующем списке должны быть в нижнем регистре.
# Например, существуют 2 списка:
# fruits_1 = [‘banana’, ‘APPLE’, ‘watermelon’, ‘cherry’]
# fruits_2 = [‘Mango’, ‘apple’, ‘orange’, ‘cherry’]
# То вызов функции common_strings(fruits_1, fruits_2) должен вернуть [‘apple’, ‘cherry’].


# def common_strings(list1, list2, ignore_case=True):
    # common_names_ls = []
    # if ignore_case:
    #     for i in list1:
    #         for j in list2:
    #             if i.lower() == j.lower():
    #                 common_names_ls.append(i.lower())
    # else:
    #     for i in list1:
    #         for j in list2:
    #             if i == j:
    #                 common_names_ls.append(i)
    #
    # return common_names_ls
#     if ignore_case:
#         set1 = {item.lower() for item in list1}
#         set2 = {item.lower() for item in list2}
#     else:
#         set1 = set(list1)
#         set2 = set(list2)
#
#     result = set1.intersection(set2)
#
#     return [item.lower() for item in result]
#
#
# fruits_1 = ['banana', 'APPLE', 'watermelon', 'cherry']
# fruits_2 = ['Mango', 'apple', 'orange', 'cherry']
# print(common_strings(fruits_1, fruits_2, ignore_case=True))
