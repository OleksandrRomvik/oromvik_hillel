# homeworks_09.py
def is_even(num):
    return num % 2 == 0

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    return sum(1 for char in s.lower() if char in 'aeiou')

def square_numbers(lst):
    return [x ** 2 for x in lst]

def filter_positive(lst):
    return [x for x in lst if x > 0]