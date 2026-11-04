class Student:
    def __init__(self, name: str, marks: list[float]) -> None:
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        if not self.marks:
            return False

        average = sum(self.marks) / len(self.marks)
        return average > 50


if __name__ == "__main__":
    student1 = Student("Alicja", [60, 70, 80])
    student2 = Student("Oskar", [30, 40, 45])

    print(student1.name, student1.is_passed())  # Alice True
    print(student2.name, student2.is_passed())  # Bob False
