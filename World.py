import random
from Combat import Combat
from Enemies import Goblin, Orc, Troll



class Scene:
    def start(self,player):
        pass

class OpeningScene(Scene):
    def start(self,player):
        print("Ξυπνάς σε ένα πανδοχείο, το κεφάλι σου μπερδεμένο. Αναρωτιέσαι πώς βρέθηκες εδώ και τι συνέβη.")
        print("Βγαίνεις απο το δωμάτιο και πηγαινεις στην ιδιοκτήτη.")
        print("Ιδιοκτητης: 'Καλημερα ξένε, εισαι καλα;")
        print(f"{player.name}: 'Δεν είμαι σίγουρος, δεν θυμάμαι τίποτα.Πώς βρέθηκα εδώ;'")
        print("Ιδιοκτητης: 'Ηρθε εχθες ενα παραξενο ατομο και σε αφησε εδω.")
        print(f"{player.name}: 'Τι εννοείς παραξενο ατομο; (ισως ειναι ο αδερφος μου;)'")
        print("(Αυτο ειναι αδυνατον πεθανε πριν 4 χρονια σε στην επιδρομη της μεδουσας.)")
        print("Ανασηκωνοντας το κεφαλι γνεφεις και ρωτας για το χωριο.")
        print("Ιδιοκτητης: Το χωριο ειναι μικρο αλλα εχει ολα τα βασικα, ενα μαγαζι για προμηθειες, μια ταβερνα για να παρεις πληροφοριες και μια εκκλησια για να προσευχηθεις.")
        input("Press Enter to continue...")
        return "village"

class Village(Scene):
    def start(self,player):
        choice = input("Φτάνεις στην κεντρικη πλατεια του χωριου. \nΜαγαζι: 1 \nΤαβερνα: 2 \nΔασος: 3\nΕπέλεξε:     ")
        if choice == "1":
            return "shop"
        elif choice == "2":
            return "tavern"
        elif choice == "3":
            return "forest"

class Shop(Scene):
    def start(self,player):
        print("Καλωσορισες στο μαγαζι, τι θελεις να αγορασεις;")
        print(f"1. Potion of Strength {random.randint(10, 20)} gold")
        print(f"2. Potion of Defense {random.randint(10, 20)} gold")
        print(f"3. Potion of Health {random.randint(10, 20)} gold")
        print(f"4. Potion of Mana {random.randint(10, 20)} gold")
        choice = input("Επέλεξε:     ")
        if choice == "1":
            print("Potion of Strength")
            print("+10 ποντοι επιθεσης")
            player.Attack += 10
            print(f"Attack: {player.Attack}")
        elif choice == "2":
            print("Potion of Defense")
            print("+10 ποντοι άμυνας")
            player.Defense += 10
            print(f"Defense: {player.Defense}")
        elif choice == "3":
            print("Potion of Health")
            print("+10 ποντοι υγειας")
            player.Health += 10
            print(f"Health: {player.Health}")
        elif choice == "4":
            print("Potion of Mana")
            print("+10 ποντοι Μανα")
            player.Mana += 10
            print(f"Mana: {player.Mana}")
        else:
            print("Invalid choice. Please select a valid option.")
        input("Press Enter to continue...")
        return "village"
    
class Tavern(Scene):
   def start(self,player): 
    print("Καλωσορισες στην ταβερνα, τι θελεις να κανεις;")
    print("1. Μιλα με τον ιδιοκτητη")  
    print("2. Μιλα με τους πελατες")
    print("3. Φύγε") 

class Forest(Scene):
    def start(self,player):
        print("Μπαίνεις στο δάσος εντονη βλαστηση σε περιτρεγυριζει, ακουγονται φωνες αλλα δεν μπορεις να τις αναγνωρισεις!")
        print("Ξαφνικα ενα πρασινο γκομπλιν πεφτει απο ενα δεντρο, εισαι αρκετα δυνατος για να το αντιμετωπισεις?!")
        print("1. Μάχη")
        print("2. Φύγε")
        choice = input("Επέλεξε:     ")
        if choice == "1":
            enemy = Goblin()
            combat = Combat(player, enemy)
            result = combat.start_battle()
            return result
        