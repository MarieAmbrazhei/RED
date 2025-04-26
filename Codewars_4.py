# https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python


def to_jaden_case(string):
    lst_str = string.split()
    lst = []
    for word in lst_str:
        lst.append(word.capitalize())
    return ' '.join(lst)
    return ' '.join(word.capitalize() for word in string.split())


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))


# https://www.codewars.com/kata/55f9b48403f6b87a7c0000bd/train/python

def paperwork(n, m):
    # if n < 0 or m < 0:
    #     return 0
    # else:
    #     return n * m
    return 0 if n < 0 or m < 0 else n * m


print(paperwork(5, 5))


# https://www.codewars.com/kata/5f70c883e10f9e0001c89673/python


def flip(d, a):
    if d == 'L':
        return sorted(a, reverse=True)
    else:
        return sorted(a)


# https://www.codewars.com/kata/55a996e0e8520afab9000055/train/python


def cookie(x):
    if isinstance(x, (int, float)) and not isinstance(x, bool):
        return "Who ate the last cookie? It was Monica!"
    elif isinstance(x, str):
        return "Who ate the last cookie? It was Zach!"
    else:
        return "Who ate the last cookie? It was the dog!"


print(cookie(False))


# https://www.codewars.com/kata/56dae9dc54c0acd29d00109a/train/python


def main(verb, noun):
    return verb + noun


# https://www.codewars.com/kata/53dc23c68a0c93699800041d/train/python


def smash(words):
    return " ".join(words).strip()


words = ['hello', 'world', 'this', 'is', 'great']
print(smash(words))


# https://www.codewars.com/kata/56676e8fabd2d1ff3000000c/train/python


def find_needle(haystack):
    # for i, w in enumerate(haystack):
    #     if w == 'needle':
    #         return f"found the needle at position {i}"
    # return False
    return f"found the needle at position {haystack.index('needle')}"


haystack = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]
print(find_needle(haystack))
