
# a.
def display_names(names):
    for name in names:
        print(name)


names = ["Anna", "John", "Kate", "Peter", "Mark"]
display_names(names)


# b. i
def multiply_by_two(numbers):
    result = []

    for number in numbers:
        result.append(number * 2)

    return result


numbers = [1, 2, 3, 4, 5]
print(multiply_by_two(numbers))


# b. ii
def multiply_by_two_comprehension(numbers):
    return [number * 2 for number in numbers]


numbers = [1, 2, 3, 4, 5]
print(multiply_by_two_comprehension(numbers))


# c.
def display_even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(number)


numbers = list(range(1, 11))
display_even_numbers(numbers)


# d.
def display_every_second(numbers):
    for i in range(0, len(numbers), 2):
        print(numbers[i])


numbers = list(range(1, 11))
display_every_second(numbers)
