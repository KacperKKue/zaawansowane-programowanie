def is_sum_greater_or_equal(first_number: int, second_number: int, third_number: int) -> bool:
    return first_number + second_number >= third_number


if __name__ == "__main__":
    result = is_sum_greater_or_equal(10, 5, 15)
    print(result)
