"""Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False.
Строку отримати за допомогою функції input()
"""


def unik_chars():
    stroka = input("Введи речення: ")
    set_chars = set(stroka.replace(" ", ""))
    print(set_chars)
    return len(set_chars) > 10


print(unik_chars())
