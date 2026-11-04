# main.py

import re
import unicodedata


def is_palindrome(text: str) -> bool:
    normalized_text = "".join(
        character.lower()
        for character in text
        if not character.isspace()
    )

    return normalized_text == normalized_text[::-1]


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Numer elementu nie może być ujemny.")

    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(2, n + 1):
        previous, current = current, previous + current

    return current


def count_vowels(text: str) -> int:
    vowels = "aeiouyąęó"
    normalized_text = unicodedata.normalize("NFC", text.lower())

    return sum(1 for character in normalized_text if character in vowels)


def calculate_discount(price: float, discount: float) -> float:
    if not 0 <= discount <= 1:
        raise ValueError("Zniżka musi być z zakresu od 0 do 1.")

    return price * (1 - discount)


def flatten_list(nested_list: list) -> list:
    flattened = []

    for element in nested_list:
        if isinstance(element, list):
            flattened.extend(flatten_list(element))
        else:
            flattened.append(element)

    return flattened


def word_frequencies(text: str) -> dict:
    words = re.findall(r"[^\W\d_]+", text.lower())

    frequencies = {}

    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1

    return frequencies


def is_prime(n: int) -> bool:
    if n < 2:
        return False

    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False

    return True
