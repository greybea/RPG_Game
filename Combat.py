import random
import time

class Combat():
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start_battle(self):
        print("-"*50)
        print(f"{self.player.name} VS {self.enemy.name:20}")
        print(f"Health: {self.player.Health:<7} |    | Health: {self.enemy.health:>7}")
        print(f"Mana:   {self.player.Mana:<7} |    | Mana:   {self.enemy.Mana:>7}")
        print("-"*50)
        while self.player.Health > 0 and self.enemy.health > 0:
            
            action = input("Επέλεξε κινηση: \n1. Attack\n2. Magic\n3. Run\nΕπέλεξε:     ")
            if action == "1":
                damage = self.player.Attack + random.randint(-5, 5)
                self.enemy.health -= damage
                print(f"{self.player.name:<15} | VS | {self.enemy.name:>15}")
                print(f"Health: {self.player.Health:<7} |    | Health: {self.enemy.health:>7}")
                print(f"Mana:   {self.player.Mana:<7} |    | Mana:   {self.enemy.Mana:>7}")

            elif action == "2":
                if self.player.Mana >= 10:
                    damage = self.player.Magic + random.randint(-5, 5)
                    self.enemy.health -= damage
                    self.player.Mana -= 10
                    print(f"{self.player.name:<15} | VS | {self.enemy.name:>15}")
                    print(f"Health: {self.player.Health:<7} |    | Health: {self.enemy.health:>7}")
                    print(f"Mana:   {self.player.Mana:<7} |    | Mana:   {self.enemy.Mana:>7}")
                    
                
                else:
                    print("Δεν έχεις αρκετo Mana!")
            elif action == "3":
                print(f"{self.player.name} φεύγει από την μάχη!")
                return "village"

            time.sleep(2)

            if self.enemy.health > 0:
                enemy_damage = self.enemy.damage + random.randint(-5, 5)
                self.player.Health -= enemy_damage
                print(f"\n{self.enemy.name} επιτίθεται και προκαλεί {enemy_damage} ζημιά στον {self.player.name}!")
                print(f"{self.player.name:<15} | VS | {self.enemy.name:>15}")
                print(f"Health: {self.player.Health:<7} |    | Health: {self.enemy.health:>7}")
                print(f"Mana:   {self.player.Mana:<7} |    | Mana:   {self.enemy.Mana:>7}")

        if not self.player.Health > 0:
            print(f"\n{self.enemy.name} νίκησε τον {self.player.name}!")
            return "defeat"
        
        
        if not self.enemy.health > 0:
            print(f"\n{self.player.name} νίκησε τον {self.enemy.name}!")
            return "victory"
        else:
            return "defeat"
        
        
        
        
        