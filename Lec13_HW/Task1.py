class Country:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    def add(self, other_country):
        new_population = self.population + other_country.population
        new_name = f"{self.name} {other_country.name}"
        return Country(new_name, new_population)

    def __str__(self):
        return f"Name: {self.name}, population: {self.population}"


if __name__ == "__main__":
    bosnia = Country("Bosnia", 10_000_000)
    herzegovina = Country("Herzegovina", 5_000_000)
    bosnia_herzegovina = bosnia.add(herzegovina)
    print(bosnia_herzegovina)
