class Pet:
    """
        This is the Pet class
    """
    def __init__(self, name: str, animal_type: str):
        """
            This is the variable initialization in the variables of the Pet class
        """
        self.name = name
        self.animal_type = animal_type

    def make_sound(self) -> str:
        """
            This is the function that makes sound 
        """
        if self.animal_type == "dog":
            return "Woof!"
        elif self.animal_type == "cat":
            return "Meow!"
        else:
            return "Unknown sound"

# Don't change the following code
print(Pet.__doc__)
print(Pet.__init__.__doc__)
print(Pet.make_sound.__doc__)
