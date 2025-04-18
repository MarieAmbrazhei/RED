https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python


def to_jaden_case(string):
    lst_str = string.split()
    lst = []
    for word in lst_str:
        lst.append(word.capitalize())
    return ' '.join(lst)
    return ' '.join(word.capitalize() for word in string.split())

print(to_jaden_case("How can mirrors be real if our eyes aren't real"))

