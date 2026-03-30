class Enemies:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        self.Mana = 100

class Goblin(Enemies):
    def __init__(self):
        super().__init__("Goblin", 80, 15)

class Orc(Enemies):
    def __init__(self):
        super().__init__("Orc", 120, 25)

class Troll(Enemies):
    def __init__(self):
        super().__init__("Troll", 150, 30)