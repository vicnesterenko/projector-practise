class Car:
    def __init__(self, brand: str, model: str, year: int, speed: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    @property
    def accelerate(self):
        return self.speed + NUM

    @property
    def brake(self):
        return self.speed - NUM

    def __str__(self):
        type_car_ride = input("Choose your car ride - city or track: ")
        if type_car_ride == "city":
            return f"Decrease speed on {NUM}. {self.brand, self.model} speed now: {self.brake}"
        else:
            return f"Increase speed on {NUM}. {self.brand, self.model} speed now: {self.accelerate}"


if __name__ == "__main__":
    NUM = 5
    MAZDA = Car("Mazda", "CX-5", 2012, 60)
    print(MAZDA)
    RANGE_ROVER = Car("Range Rover", "SV", 2023, 80)
    print(RANGE_ROVER)
