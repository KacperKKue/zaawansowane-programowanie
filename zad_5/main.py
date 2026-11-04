def contains_value(numbers: list[int], value: int) -> bool:
    return value in numbers


if __name__ == "__main__":
    print(contains_value([1, 2, 3, 4], 3))  # True
    print(contains_value([1, 2, 3, 4], 8))  # False
