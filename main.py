from Player import  Warrior, Mage, Rogue
from World import OpeningScene, Village , Shop , Tavern, Forest

classes = { 
    '1': Warrior,
    '2': Mage,
    '3': Rogue
}

scenes_map = {
    'opening_scene': OpeningScene(),
    'village': Village(),
    'shop': Shop(),
    'tavern': Tavern(),
    'forest': Forest()
}

print("Welcome to Ritual Stone!")
name = input("What is your name? ")
print("What is your Class?")
print("1. Warrior")
print("2. Mage")
print("3. Rogue")
x = input("Select your class (1-3): ")
if x in classes:
        player = classes[x](name)
        print(f"You have selected {player.__class__.__name__} class.")
        print(f"Name: {player.name}, \nAttack: {player.Attack}, \nDefense: {player.Defense}, \nHealth: {player.Health}, \nMana: {player.Mana}, \nAgility: {player.Agility}, \nMagic: {player.Magic}")
        
else:
     while x not in ['1', '2', '3']:
        print("Invalid choice. Please select a valid class (1-3).")
        x = input("Select your class (1-3): ")
        if x in classes:
            player = classes[x](name)
            print(f"You have selected {player.__class__.__name__} class.")
            print(f"Name: {player.name}, \nAttack: {player.Attack}, \nDefense: {player.Defense}, \nHealth: {player.Health}, \nMana: {player.Mana}, \nAgility: {player.Agility}, \nMagic: {player.Magic}")

current_scene = 'opening_scene'
while current_scene not in ['victory', 'defeat']:
    scene_obj = scenes_map[current_scene]
    current_scene = scene_obj.start(player)

