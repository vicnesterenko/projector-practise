class Car:
    def __init__(self, brand: str, model: str, year: int, speed: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self, num):
        self.speed += num

    def brake(self, num):
        self.speed -= num

    def __str__(self):
        return f"Car: {self.brand} {self.model}, Year: {self.year}, Speed: {self.speed}"


if __name__ == "__main__":
    MAZDA = Car("Mazda", "CX-5", 2012, 60)
    RANGE_ROVER = Car("Range Rover", "SV", 2023, 80)

    while True:
        try:
            type_car_ride = input(
                "Choose your car ride - city or track (or type 'exit' to quit): "
            )
            if type_car_ride == "exit":
                break
            elif type_car_ride == "city":
                MAZDA.brake(5)
                RANGE_ROVER.brake(5)
            elif type_car_ride == "track":
                MAZDA.accelerate(5)
                RANGE_ROVER.accelerate(5)
            else:
                print("Invalid input. Please choose 'city' or 'track'")

            print(MAZDA)
            print(RANGE_ROVER)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
