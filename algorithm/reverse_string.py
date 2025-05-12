# 1 Напишите функцию, которая переворачивает строку, то есть возвращает строку,
# где символы расположены в обратном порядке.
# Входные данные:
# Одна строка s.
# Выходные данные:
# Строка, содержащая символы исходной строки в обратном порядке.
# Пример:
# Вход: "hello"
# Выход: "olleh"
# Ограничения:
# Длина строки
# 1≤∣s∣≤10
# Строка состоит только из печатных символов (букв, цифр, знаков препинания и пробелов).


def reverse_string_manual(s):
    reversed_str = " "
    for char in range(len(s) - 1, -1, -1):
       reversed_str += s[char]
    print(reversed_str)

    reversed_str = s[::-1]
    print(reversed_str)

    reversed_str = ''.join(reversed(s))
    print(reversed_str)

    reversed_str = ""
    i = len(s) - 1
    while i >= 0:
        reversed_str += s[i]
        i = i - 1
    return reversed_str

    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str


print(reverse_string_manual('Hello'))
