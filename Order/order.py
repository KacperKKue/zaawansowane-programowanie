from utils import utils


class Order:
    def __init__(self, order_id: int, product: object):
        self.order_id = order_id
        self.product = product

    def __str__(self) -> str:
        return (
            f"Zamówienie nr {self.order_id}: "
            f"{self.product.name}"
        )

    def display(self) -> None:
        utils.display_message(str(self))
