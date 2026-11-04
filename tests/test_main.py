# test_main.py

import unittest

from main import (
    is_palindrome,
    fibonacci,
    count_vowels,
    calculate_discount,
    flatten_list,
    word_frequencies,
    is_prime,
)


class TestIsPalindrome(unittest.TestCase):

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("kajak"))
        self.assertTrue(is_palindrome("Kobyła ma mały bok"))
        self.assertFalse(is_palindrome("python"))
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("A"))


class TestFibonacci(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)


class TestCountVowels(unittest.TestCase):

    def test_count_vowels(self):
        self.assertEqual(count_vowels("Python"), 2)
        self.assertEqual(count_vowels("AEIOUY"), 6)
        self.assertEqual(count_vowels("bcd"), 0)
        self.assertEqual(count_vowels(""), 0)
        self.assertEqual(count_vowels("Próba żółwia"), 5)


class TestCalculateDiscount(unittest.TestCase):

    def test_calculate_discount(self):
        self.assertEqual(calculate_discount(100, 0.2), 80.0)
        self.assertEqual(calculate_discount(50, 0), 50.0)
        self.assertEqual(calculate_discount(200, 1), 0.0)

    def test_invalid_discount(self):
        with self.assertRaises(ValueError):
            calculate_discount(100, -0.1)

        with self.assertRaises(ValueError):
            calculate_discount(100, 1.5)


class TestFlattenList(unittest.TestCase):

    def test_flatten_list(self):
        self.assertEqual(
            flatten_list([1, 2, 3]),
            [1, 2, 3]
        )

        self.assertEqual(
            flatten_list([1, [2, 3], [4, [5]]]),
            [1, 2, 3, 4, 5]
        )

        self.assertEqual(flatten_list([]), [])

        self.assertEqual(flatten_list([[[1]]]), [1])

        self.assertEqual(
            flatten_list([1, [2, [3, [4]]]]),
            [1, 2, 3, 4]
        )


class TestWordFrequencies(unittest.TestCase):

    def test_word_frequencies(self):
        self.assertEqual(
            word_frequencies("To be or not to be"),
            {"to": 2, "be": 2, "or": 1, "not": 1}
        )

        self.assertEqual(
            word_frequencies("Hello, hello!"),
            {"hello": 2}
        )

        self.assertEqual(word_frequencies(""), {})

        self.assertEqual(
            word_frequencies("Python Python python"),
            {"python": 3}
        )

        self.assertEqual(
            word_frequencies("Ala ma kota, a kot ma Ale."),
            {"ala": 1, "ma": 2, "kota": 1, "a": 1, "kot": 1, "ale": 1}
        )


class TestIsPrime(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(97))


if __name__ == "__main__":
    unittest.main()