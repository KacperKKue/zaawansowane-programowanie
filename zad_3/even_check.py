def is_even(number: int) -> bool:
    return number % 2 == 0


if __name__ == "__main__":
    number = 12
    even = is_even(number)

    if even:
        print("Liczba parzysta")
    else:
        print("Liczba nieparzysta")
