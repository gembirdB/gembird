from collections import Counter


def anagram(first, second):
    return Counter(first) == Counter(second)

anagram("пират", "тапир")
>>> True
