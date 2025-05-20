# test_homeworks_09.py
# pytest lesson_09/test_homeworks_09.py -v
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from homeworks_09 import *


class TestHomeworkFunctions:
    def test_is_even_true(self):
        assert is_even(4)

    def test_is_even_false(self):
        assert not is_even(5)

    def test_reverse_string(self):
        result = reverse_string("hello")
        assert isinstance(result, str)
        assert result == "olleh"

    def test_count_vowels(self):
        assert count_vowels("Education") == 5

    def test_count_vowels_empty(self):
        assert count_vowels("") == 0

    def test_square_numbers(self):
        result = square_numbers([1, 2, 3])
        assert result == [1, 4, 9]
        assert len(result) == 3

    def test_square_numbers_empty(self):
        assert square_numbers([]) == []

    def test_filter_positive_mixed(self):
        result = filter_positive([-2, 0, 3, -1, 5])
        assert 3 in result
        assert -2 not in result
        assert result == [3, 5]

    def test_filter_positive_all_positive(self):
        assert all(x > 0 for x in filter_positive([1, 2, 3]))

    def test_filter_positive_all_negative(self):
        result = filter_positive([-5, -1])
        assert result == []
        assert isinstance(result, list)
