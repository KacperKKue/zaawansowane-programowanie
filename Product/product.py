from utils import utils


class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f"Produkt: {self.name}, cena: {self.price} zł"

    def display(self) -> None:
        utils.display_message(str(self))
