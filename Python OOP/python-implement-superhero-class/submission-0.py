class SuperHero:
    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """

    def __init__(self, name: str, power: str, health: int):
        # TODO: Initialize the superhero's attributes here
        self.name = name
        self.power = power
        self.health = health


# TODO: Create Superhero instances
superhero_batman = SuperHero("Batman", "Intelligence", 100)
superhero_superman = SuperHero("Superman", "Strength", 150)


# TODO: Print out the attributes of each superhero
print(superhero_batman.name)
print(superhero_batman.power)
print(superhero_batman.health)

print(superhero_superman.name)
print(superhero_superman.power)
print(superhero_superman.health)
