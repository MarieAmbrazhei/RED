# 1
# Магазин.
# Есть словарь с товарами:
# products = {
#      "apple": {"quantity": 10, "price": 100},
#     "banana": {"quantity": 20, "price": 50},
#     "orange": {"quantity": 15, "price": 80},
#     "grape": {"quantity": 8, "price": 120},
#     "milk":{"quantity": 12, "price": 90},
#      "bread": {"quantity": 30, "price": 40}
# }
# Необходимо увеличить цену всех продуктов на 20 процентов.
# Удалить товар “milk”.
# Добавить товар “Salt” с количеством 7 и ценой 12.
# Вывести общую стоимость всех товаров в магазине.
# Ответ: 6516.0

def modify_dict(d, percentage):
    for key, value in d.items():
        value['price'] *= (1 + percentage / 100)
    d.pop('milk')
    d['Salt'] = {"quantity": 7, "price": 12}

    total_sum = 0
    for key, value in d.items():
        total_sum += value["quantity"] * value['price']

    return total_sum


products = {
    "apple": {"quantity": 10, "price": 100},
    "banana": {"quantity": 20, "price": 50},
    "orange": {"quantity": 15, "price": 80},
    "grape": {"quantity": 8, "price": 120},
    "milk": {"quantity": 12, "price": 90},
    "bread": {"quantity": 30, "price": 40}
}

print(modify_dict(products, 20))

# 2
# Alice.
# Есть два списка одинаковой длины:
# keys = ['name', 'age', 'city', 'occupation', 'email', 'phone', 'hobby', 'education', 'company', 'salary']
# values = ['Alice', 30, 'New York', 'Engineer', 'alice@example.com', '+1234567890', 'Reading', 'Masters in Computer Science', 'TechCorp', 90000]
# Создайте словарь info из ключей keys и значений values. (Каждое значение занимает ту же позицию, что и ключ в другом списке)
# Выведите словарь info на экран.

from itertools import zip_longest


def generate_new_dict(lst1: list, lst2: list) -> dict:
    # return dict(zip(lst1, lst2))
    # return dict(zip_longest(lst1, lst2))
    info = {}
    for i in range(len(lst1)):
        info[lst1[i]] = lst2[i]
    return info


keys = ['name', 'age', 'city', 'occupation', 'email', 'phone', 'hobby', 'education', 'company',
        'salary']
values = ['Alice', 30, 'New York', 'Engineer', 'alice@example.com', '+1234567890', 'Reading',
          'Masters in Computer Science', 'TechCorp', 90000]
new_dict = generate_new_dict(keys, values)
print(new_dict)


# Шифр.
# Есть сообщение (строка):
# "2__234йшDGмёшSDFжкъrrrщзнSDF78юкйфуSDFшёью$#2Sшжйи3%узфsdf34нкфыvvя"
# И ключ к шифру, где каждую букву нужно заменить на ее значение в словаре:
# cipher = {
#     "а": "щ", "б": "д", "в": "ю", "г": "ф", "д": "з", "е": "м", "ё": "р",
#     "ж": "т", "з": "п", "и": "я", "й": "с", "к": "н", "л": "э", "м": "к",
#     "н": "л", "о": "ё", "п": "ж", "р": "ц", "с": "б", "т": "у", "у": "в",
#     "ф": "о", "х": "и", "ц": "х", "ч": "г", "ш": "е", "щ": "й", "ъ": "ы",
#     "ы": "ч", "ь": "ш", "э": "ъ", "ю": "а", "я": "ь"
# }
# Расшифруйте секретное сообщение с помощью ключа cipher, при этом мусорные значение (которых нет в словаре) должны быть пропущены и не добавлены в результат.
# Выведите результат на экран.
# Дополнительно: напишите программу, которая получает строку через ввод с клавиатуры и “отправляет” зашифрованный ответ агенту.


def decrypt_the_message(my_str: str, cipher: dict) -> str:
    # message = ''
    # for i in my_str.lower():
    #     if i in cipher and i.isalpha():
    #         message += cipher[i]
    # print(message)
    # return message
    return ''.join(cipher[i] for i in my_str.lower() if i in cipher and i.isalpha())


def crypt_the_message(cipher: dict) -> str:
    new_cipher = {v: k for k, v in cipher.items()}
    encrypted_message = ''
    message = input("Введите сообщение для шифровки: ").lower()
    # for i in message:
    #     if i in new_cipher:
    #         encrypted_message += new_cipher[i]
    # return encrypted_message
    return ''.join(new_cipher[i] for i in message if i in new_cipher)


mixed_str = "2__234йшDGмёшSDFжкъrrrщзнSDF78юкйфуSDFшёью$#2Sшжйи3%узфsdf34нкфыvvя"

cipher = {
    "а": "щ", "б": "д", "в": "ю", "г": "ф", "д": "з", "е": "м", "ё": "р",
    "ж": "т", "з": "п", "и": "я", "й": "с", "к": "н", "л": "э", "м": "к",
    "н": "л", "о": "ё", "п": "ж", "р": "ц", "с": "б", "т": "у", "у": "в",
    "ф": "о", "х": "и", "ц": "х", "ч": "г", "ш": "е", "щ": "й", "ъ": "ы",
    "ы": "ч", "ь": "ш", "э": "ъ", "ю": "а", "я": "ь"
}
secret_message = decrypt_the_message(mixed_str, cipher)
print("Расшифрованное сообщение:")
print(secret_message)
crypted_mes = crypt_the_message(cipher)
print("Зашифрованное сообщение:")
print(crypted_mes)


# 4*
# Самая популярная буква.
# Есть строка:
# dialog = """Doc: Запомни! Согласно моей теории, ты помешал знакомству своих родителей.
# Если они не встретятся, то не влюбятся, не поженятся, и у них не будет детей.
# Поэтому твой старший брат исчезает с фотографии. Затем очередь твоей сестры,
# и если ты все не исправишь, ты будешь следующим.
# Marty: Тяжелый случай.
# Doc: Вес тут совершенно ни при чем. """
# # Тройные кавычки позволяют удобно писать текст в несколько строк.


def the_most_popular_letter(my_str: str):
    my_dict = {}
    # 1
    # for letter in my_str.lower():
    #     if letter.isalpha():
    #         my_dict[letter] = my_dict.get(letter, 0) + 1
    # return my_dict
    # 2
    # for letter in my_str.lower():
    #     if letter.isalpha():
    #         if letter in my_dict:
    #             my_dict[letter] += 1
    #         else:
    #             my_dict[letter] = 1
    # return my_dict
    # 3
    # for letter in my_str:
    #     if letter.isalpha():
    #         my_dict.setdefault(letter.lower(), 0)
    #         my_dict[letter.lower()] += 1
    # print(my_dict)
    # max_letter = max(my_dict, key=my_dict.get)
    # return max_letter, my_dict[max_letter]


dialog = """Doc: Запомни! Согласно моей теории, ты помешал знакомству своих родителей.
Если они не встретятся, то не влюбятся, не поженятся, и у них не будет детей.
Поэтому твой старший брат исчезает с фотографии. Затем очередь твоей сестры,
и если ты все не исправишь, ты будешь следующим.
Marty: Тяжелый случай.
Doc: Вес тут совершенно ни при чем. """
new_dict = the_most_popular_letter(dialog)
print(new_dict)
