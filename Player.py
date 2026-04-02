import json

class Player:
    def __init__(self, name, inventory = None,current_scene = 'opening_scene'):
        self.inventory = inventory if inventory is not None else []
        self.name = name
        self.current_scene = current_scene
        self.Attack = 0
        self.Defense = 0
        self.Health = 0
        self.Mana = 0
        self.Agility = 0
        self.Magic = 0
    
    def save(self):
        with open('save.json', 'w', encoding='utf-8') as file:
            json.dump(self.to_dict(), file, indent=4 , ensure_ascii=False)

    def change_scene(self, new_scene):
        self.current_scene = new_scene
        self.save()
        print(f"Scene changed to {new_scene}. Game saved.")
    def to_dict(self):
        return {
            'class': self.__class__.__name__,
            'name': self.name,
            'inventory': self.inventory,
            'Attack': self.Attack,
            'Defense': self.Defense,
            'Health': self.Health,
            'Mana': self.Mana,
            'Agility': self.Agility,
            'Magic': self.Magic,
            'current_scene': self.current_scene
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
        