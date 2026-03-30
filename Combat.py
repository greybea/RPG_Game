import random
import time

class Combat():
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start_battle(self):
        print(f"{self.player.name} VS {self.enemy.name}!")
        while self.player.Health > 0 and self.enemy.Health > 0:
            print(f"{self.player.name}\n Health: {self.player.Health}\n Mana: {self.player.Mana}")
            print(f"{self.enemy.name}\n Health: {self.enemy.Health}\n Mana: {self.enemy.Mana}")
            action = input("Επέλεξε κινηση: \n1. Attack\n2. Magic\n3. Run\nΕπέλεξε:     ")
            if action == "1":
                damage = self.player.Attack + random.randint(-5, 5)
                self.enemy.Health -= damage
                print(f"{self.player.name} επιτίθεται και προκαλεί {damage} ζημιά στον {self.enemy.name}!")
                print(f"{self.player.name}\n Health: {self.player.Health}\n Mana: {self.player.Mana}")
                print(f"{self.enemy.name} \n Health: {self.enemy.Health} \n Mana: {self.enemy.Mana}")
            elif action == "2":
                if self.player.Mana >= 10:
                    damage = self.player.Magic + random.randint(-5, 5)
                    self.enemy.Health -= damage
                    self.player.Mana -= 10
                    print(f"{self.player.name} χρησιμοποιεί μαγεία και προκαλεί {damage} ζημιά στον {self.enemy.name}!")
                    print(f"{self.player.name}\n Health: {self.player.Health}\n Mana: {self.player.Mana}")
                    print(f"{self.enemy.name} \n Health: {self.enemy.Health} \n Mana: {self.enemy.Mana}")
                else:
                    print("Δεν έχεις αρκετo Mana!")
            elif action == "3":
                print(f"{self.player.name} φεύγει από την μάχη!")
                break
        
        if not self.enemy.Health > 0:
            print(f"{self.player.name} νίκησε τον {self.enemy.name}!")
            return "victory"
        
        time.sleep(1)

        enemy_damage = self.enemy.damage + random.randint(-5, 5)
        self.player.Health -= enemy_damage
        print(f"{self.enemy.name} επιτίθεται και προκαλεί {enemy_damage} ζημιά στον {self.player.name}!")
        print(f"{self.player.name}\n Health: {self.player.Health}\n Mana: {self.player.Mana}")
        print(f"{self.enemy.name} \n Health: {self.enemy.Health} \n Mana: {self.enemy.Mana}")

        if not self.player.Health > 0:
            print(f"{self.enemy.name} νίκησε τον {self.player.name}!")
            return "defeat"
        
        time.sleep(1)