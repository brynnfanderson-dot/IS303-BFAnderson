class pet:
    max_happiness = 50
    max_hunger = 10
    
    def __init__(self, pet_name, animal_type, hunger, happiness, bond):
        self.name = pet_name
        self.type = animal_type
        self.hunger = hunger
        self.happiness = happiness
        self.bond = bond

    def play(self):
        self.happiness += 10
        self.hunger -= 5

    def eat(self):
        self.hunger += 10
        self.bond +=3