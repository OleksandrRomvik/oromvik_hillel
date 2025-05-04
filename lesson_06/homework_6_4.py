"""Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті"""

lst_of_num = [2, 3, 4, 5, 6, 7, 8, 88, 755, 45, 33, 22]
count_par_num = 0
for num in lst_of_num:
    if num % 2 == 0:
        count_par_num += num

print(count_par_num)
