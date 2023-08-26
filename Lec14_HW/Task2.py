class Restaurant:
    def __init__(self, name: str, cuisine: str, menu: dict) -> None:
        self.name = name
        self.cuisine = cuisine
        self.menu = menu


class FastFood(Restaurant):
    def __init__(self, name: str, cuisine: str, menu: dict, drive_thru: bool) -> None:
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru

    def order(self, dish_name: str, quantity: int):
        # if not isinstance(dish_name, Restaurant):
        #    raise ValueError("Dish not available")
        if dish_name not in self.menu:
            return "Dish not available"

        dish_details = self.menu[dish_name]
        # print(dish_details["quantity"])
        if quantity > dish_details["quantity"]:
            return "Requested quantity not available"

        total_cost = dish_details["price"] * quantity
        dish_details["quantity"] -= quantity
        return f"Your order is ready! Total price = {total_cost}"


if __name__ == "__main__":
    menu = {
        "burger": {"price": 5, "quantity": 10},
        "pizza": {"price": 10, "quantity": 20},
        "drink": {"price": 1, "quantity": 15},
    }

    mc = FastFood("McDonalds", "Fast Food", menu, True)

    print("First order:", mc.order("burger", 5))  # 25
    print("Second order:", mc.order("burger", 15))  # Requested quantity not available
    print("Third order:", mc.order("soup", 5))  # Dish not available
