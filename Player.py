import json

class Player:
    def __init__(self, name, inventory):
        self.inventory = []
        self.name = name
    
    def to_dict(self):
        return {
            'name': self.name,
            'inventory': self.inventory,
            'Attack': self.Attack,
            'Defense': self.Defense,
            'Health': self.Health,
            'Mana': self.Mana,
            'Agility': self.Agility,
            'Magic': self.Magic
        }
class Warrior(Player):
    def __init__(self, name):
        super().__init__(name, [10])
        self.Attack = 40
        self.Defense = 40 
        self.Health = 100
        self.Mana = 100
        self.Agility = 20
        self.Magic = 20
        

class Mage(Player):
    def __init__(self, name):
        super().__init__(name, [10])
        self.Attack = 20
        self.Defense = 20
        self.Health = 80
        self.Mana = 100
        self.Agility = 20
        self.Magic = 45
        

class Rogue(Player):
    def __init__(self, name):
        super().__init__(name, [10])
        self.Attack = 30
        self.Defense = 30
        self.Health = 90
        self.Mana = 100
        self.Agility = 40
        self.Magic = 20
        