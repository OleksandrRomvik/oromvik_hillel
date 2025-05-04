# task 1
"""Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
import math

print("\ntask 1 ----------------------------------------")


def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1
    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if result > 25:
            # Enter the action to take if the result is greater than 25
            break
            pass
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1
        # Increment the appropriate variable


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
print("\ntask 2 ----------------------------------------")
"""  Написати функцію, яка обчислює суму двох чисел.
"""


def sum_two_int(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        result = a + b
        print(result)
    else:
        print("Помилка: потрібно ввести два числа")


sum_two_int(5, 4)


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

print("\ntask 3 ----------------------------------------")


def aver_two_int(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        result = (a + b) / 2
        print(result)
    else:
        print("Помилка: потрібно ввести два числа")


aver_two_int(5, 5)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

print("\ntask 4 ----------------------------------------")


def rev_str(s):
    if isinstance(s, str):
        return s[::-1]
    else:
        return "Помилка: введіть рядок"


print(rev_str("Рядок"))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

print("\ntask 5 ----------------------------------------")


def longest_word_of_list(words):
    if isinstance(words, list):
        return max(words, key=len)
    else:
        return "Помилка: введіть список слів"


print(longest_word_of_list(["Рядок", "в", "реченні", "як", "приклад."]))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

print("\ntask 6 ----------------------------------------")


def find_substring(str1, str2):
    return str1.find(str2)


str1 = "Hello, world!"
str2 = "world"
# str1 = "The quick brown fox jumps over the lazy dog"
# str2 = "cat"
print(find_substring(str1, str2))  # поверне 7
# print(find_substring(str1, str2)) # поверне -1


# task 7 Знайди остачу від діленя чисел
print("\ntask 7 ----------------------------------------")


def ostacha_vid_dilenn(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        result = a % b
        return result
    else:
        print("Ви ввели некорректні значення")


print(ostacha_vid_dilenn(11, 5))

# task 8
# Виведіть, скільки слів у тексті починається з Великої літери?
print("\ntask 8 ----------------------------------------")


def words_by_title(sentence):

    if isinstance(sentence, str):
        words = sentence.split()  # розбиваємо рядок на слова
        count = 0
        for word in words:
            if word[0].isupper():  # якщо перша літера слова велика до в count+1
                count += 1
        return count
    else:
        return "Помилка: введіть текст"


print(
    words_by_title(
        "By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for."
    )
)


# task 9
print("\ntask 9 ----------------------------------------")
"""Мережа супермаркетів має 3 склади, де всього розміщено
375291 товар. На першому та другому складах перебуває
250449 товарів. На другому та третьому – 222950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі."""


def items_per_warehouse(all_items, items_on_1_and_2, items_on_2_and_3):
    warehouse1 = 0
    warehouse2 = 0
    warehouse3 = 0
    if (
        isinstance(all_items, int)
        and isinstance(items_on_1_and_2, int)
        and isinstance(items_on_2_and_3, int)
    ):
        warehouse1 = all_items - items_on_2_and_3
        warehouse3 = all_items - items_on_1_and_2
        warehouse2 = all_items - warehouse1 - warehouse3
        return print(
            f"На першому складі = {warehouse1}, другому = {warehouse2}, третьому= {warehouse3} товарів"
        )

    else:
        print("Ви ввели некорректні значення кількості товарів")


items_per_warehouse(375291, 250449, 222950)

# task 10
print("\ntask 10 ----------------------------------------")
"""Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?"""


def album_size(fotos):
    fotos_per_page = 8
    result = math.ceil(fotos / fotos_per_page)
    return result


while True:
    user_input = input("Введи кількість фотографій: ")
    if user_input.isdigit():  # перевіряємо, що це ціле число
        fotos = int(user_input)
        pages = album_size(fotos)
        print(f"Ігорю знадобиться {pages} сторінок.")
        break
    else:
        print("Помилка! Введи ціле число, наприклад: 232")

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
