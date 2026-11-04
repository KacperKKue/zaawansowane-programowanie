def merge_unique_cubed(first: list[int], second: list[int]) -> list[int]:
    combined = first + second
    unique_numbers = dict.fromkeys(combined)

    return [number ** 3 for number in unique_numbers]


if __name__ == "__main__":
    print(merge_unique_cubed([1, 2, 3], [3, 4, 2]))
    # [1, 8, 27, 64]
