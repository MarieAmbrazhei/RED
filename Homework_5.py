# 1
# Продвинутый sum.
# Встроенная функция sum() в python вызывает ошибку, если один из элементов последовательности не является числом, например sum([1, 2, ‘A’]).
# Напишите функцию sum_ignore_non_numbers(), которая имеет один параметр items (список или кортеж).
# Функция должна вернуть сумму всех чисел (int, float) в переданной последовательности. При этом все нечисловые значения должны игнорироваться.
# Если чисел нет, то функция должна вернуть 0.
# Если вызвать функцию со списком [1, 2, 'Hey', None, 4.3], то она должна вернуть 7.3


def sum_ignore_non_numbers(items):
    # return [sum(num for num in items if isinstance(num, (int, float)))]
    count = 0
    for num in items:
        if isinstance(num,(int, float)):
            count += num
    return count


print(sum_ignore_non_numbers([1, 2, 'A']))
