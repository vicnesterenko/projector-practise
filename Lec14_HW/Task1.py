class Product:
    def __init__(self, name: str, price: int, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity


class Book(Product):
    def __init__(self, name: str, price: int, quantity: int, author: str):
        super().__init__(name, price, quantity)
        self.author = author

    def read(self):
        print(
            "Welcome to Book Store!",
            "We have the book you need for Python learning:",
            f"{self.name} by {self.author}",
            f"Price: {self.price}₴, Quantity: {self.quantity}",
            sep="\n",
        )


if __name__ == "__main__":
    book = Book("Fluent Python", 3329, 10, "Luciano Ramalho")
    book.read()
