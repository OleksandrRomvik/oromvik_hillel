from itertools import count

adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.split()
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer)
print(adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print(adwentures_of_tom_sawer.count("h"))

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
text = adwentures_of_tom_sawer.split()
up_words = 0
for word in text:
    if word[0].isupper():
        up_words = up_words + 1
print(up_words)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
# first_index=adwentures_of_tom_sawer.find("Tom")
# if first_index !=-1:
#     second_index=adwentures_of_tom_sawer.find("Tom",first_index+1)
#     print(second_index)

index = adwentures_of_tom_sawer.find("Tom")
if index != -1:
    index = adwentures_of_tom_sawer.find("Tom", index + 1)
    print(index)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(".")
adwentures_of_tom_sawer_sentences = [s for s in adwentures_of_tom_sawer_sentences if s.strip()]
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print(adwentures_of_tom_sawer_sentences[3])
adwentures_of_tom_sawer_sentences_join = ".".join(adwentures_of_tom_sawer_sentences)
adwentures_of_tom_sawer_sentences_lower = adwentures_of_tom_sawer_sentences_join.lower()
print(adwentures_of_tom_sawer_sentences_lower)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
find_by = adwentures_of_tom_sawer.find("By the time")
if find_by != -1:
    print("Так, є речення що починається з \"By the time\"")
else:
    print("Таке речення відсутнє")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print(adwentures_of_tom_sawer_sentences)
last_sentence = adwentures_of_tom_sawer_sentences[-1]
word_count = len(last_sentence.split())
print("Кількість слів:", word_count)



