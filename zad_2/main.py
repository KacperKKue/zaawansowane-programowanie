
from datetime import date


class Library:
    def __init__(
        self,
        city: str,
        street: str,
        zip_code: str,
        open_hours: str,
        phone: str,
    ) -> None:
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self) -> str:
        return (
            f"Biblioteka: {self.city}, ul. {self.street}\n"
            f"Kod pocztowy: {self.zip_code}\n"
            f"Godziny otwarcia: {self.open_hours}\n"
            f"Telefon: {self.phone}"
        )


class Employee:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        hire_date: date,
        birth_date: date,
        city: str,
        street: str,
        zip_code: str,
        phone: str,
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self) -> str:
        return (
            f"Pracownik: {self.first_name} {self.last_name}\n"
            f"Data zatrudnienia: {self.hire_date}\n"
            f"Data urodzenia: {self.birth_date}\n"
            f"Adres: ul. {self.street}, {self.zip_code} {self.city}\n"
            f"Telefon: {self.phone}"
        )


class Student:
    def __init__(self, name: str, student_id: int) -> None:
        self.name = name
        self.student_id = student_id

    def __str__(self) -> str:
        return f"Student: {self.name}, numer ID: {self.student_id}"


class Book:
    def __init__(
        self,
        library: Library,
        publication_date: date,
        author_name: str,
        author_surname: str,
        number_of_pages: int,
    ) -> None:
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self) -> str:
        return (
            f"Książka: {self.author_name} {self.author_surname}\n"
            f"Data publikacji: {self.publication_date}\n"
            f"Liczba stron: {self.number_of_pages}\n"
            f"{self.library}"
        )


class Order:
    def __init__(
        self,
        employee: Employee,
        student: Student,
        books: list[Book],
        order_date: date,
    ) -> None:
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self) -> str:
        books_description = "\n\n".join(
            str(book) for book in self.books
        )

        return (
            f"ZAMÓWIENIE\n"
            f"Data zamówienia: {self.order_date}\n\n"
            f"PRACOWNIK:\n{self.employee}\n\n"
            f"STUDENT:\n{self.student}\n\n"
            f"KSIĄŻKI:\n{books_description}"
        )


if __name__ == "__main__":
    library1 = Library(
        "Warszawa", "Długa 1", "00-001",
        "09:00-17:00", "123-456-789"
    )
    library2 = Library(
        "Kraków", "Floriańska 5", "30-000",
        "10:00-18:00", "987-654-321"
    )

    employee1 = Employee(
        "Anna", "Kowalska",
        date(2020, 5, 10), date(1990, 2, 15),
        "Warszawa", "Zielona 2", "00-002", "111-222-333"
    )
    employee2 = Employee(
        "Piotr", "Wiśniewski",
        date(2021, 3, 1), date(1988, 7, 20),
        "Kraków", "Kwiatowa 4", "30-002", "222-333-444"
    )
    employee3 = Employee(
        "Maria", "Nowak",
        date(2019, 9, 15), date(1992, 11, 5),
        "Warszawa", "Polna 6", "00-003", "333-444-555"
    )

    student1 = Student("Katarzyna Zielińska", 1001)
    student2 = Student("Tomasz Wójcik", 1002)
    student3 = Student("Magdalena Kamińska", 1003)

    book1 = Book(
        library1, date(2001, 1, 1),
        "Andrzej", "Sapkowski", 400
    )
    book2 = Book(
        library1, date(1949, 6, 8),
        "George", "Orwell", 328
    )
    book3 = Book(
        library2, date(1997, 6, 26),
        "Joanne", "Rowling", 320
    )
    book4 = Book(
        library2, date(1813, 1, 28),
        "Jane", "Austen", 279
    )
    book5 = Book(
        library1, date(1925, 4, 10),
        "Adam", "Mickiewicz", 180
    )

    order1 = Order(
        employee1, student1, [book1, book2],
        date.today()
    )
    order2 = Order(
        employee2, student2, [book3, book4, book5],
        date.today()
    )

    print(order1)
    print("=" * 60)
    print(order2)
