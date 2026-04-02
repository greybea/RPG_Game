
from Player import Warrior , Mage , Rogue
from World import OpeningScene, Village , Shop , Tavern, Forest
import json

classes = {
    'Warrior': Warrior,
    'Mage': Mage,
    'Rogue': Rogue
}

scenes_map = {
    'opening_scene': OpeningScene(),
    'village': Village(),
    'shop': Shop(),
    'tavern': Tavern(),
    'forest': Forest()
}

print("*"*50)
print("Ritual Stone")
print("*"*50)
print("1. New game")
print("2. Load game")
choice = input("Eπελεξε 1/2:")
while choice not in ['1','2']:
    print("Επελεξε 1 ή 2:")
    choice=input(" ")



if choice == "1":
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
        current_scene = 'opening_scene'
        while current_scene not in ['victory', 'defeat']:
            scene_obj = scenes_map[current_scene]
            current_scene = scene_obj.start(player)
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







