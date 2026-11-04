
class Property:
    def __init__(
        self,
        area: float,
        rooms: int,
        price: float,
        address: str,
    ) -> None:
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self) -> str:
        return (
            f"Adres: {self.address}\n"
            f"Powierzchnia: {self.area} m²\n"
            f"Liczba pokoi: {self.rooms}\n"
            f"Cena: {self.price:.2f} zł"
        )


class House(Property):
    def __init__(
        self,
        area: float,
        rooms: int,
        price: float,
        address: str,
        plot: int,
    ) -> None:
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self) -> str:
        return (
            f"DOM\n{super().__str__()}\n"
            f"Powierzchnia działki: {self.plot} m²"
        )


class Flat(Property):
    def __init__(
        self,
        area: float,
        rooms: int,
        price: float,
        address: str,
        floor: int,
    ) -> None:
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self) -> str:
        return (
            f"MIESZKANIE\n{super().__str__()}\n"
            f"Piętro: {self.floor}"
        )


if __name__ == "__main__":
    house = House(
        area=150.5,
        rooms=5,
        price=850000,
        address="ul. Lipowa 10, Warszawa",
        plot=600,
    )

    flat = Flat(
        area=65.0,
        rooms=3,
        price=520000,
        address="ul. Centralna 20, Kraków",
        floor=3,
    )

    print(house)
    print("-" * 40)
    print(flat)
