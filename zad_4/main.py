def check_sum(a: int, b: int, c: int) -> bool:
    return a + b >= c


if __name__ == "__main__":
    print(check_sum(3, 5, 8))   # True
    print(check_sum(2, 4, 10))  # False
