def create_greeting(name: str, surname: str) -> str:
    return f"Cześć {name} {surname}!"


if __name__ == "__main__":
    greeting = create_greeting("Jan", "Kowalski")
    print(greeting)
