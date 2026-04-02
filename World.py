import random
from Combat import Combat
from Enemies import Goblin, Orc, Troll




class Scene:
    def start(self,player):
        pass
    def __init__(self):
        self.is_fight_finished = False

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
        print("*"*50)
        print("--ΧΩΡΙΟ--")
        print("*"*50)
        player.change_scene("village")
        choice = input("Φτάνεις στην κεντρικη πλατεια του χωριου. \nΜαγαζι: 1 \nΤαβερνα: 2 \nΔασος: 3\nΕπέλεξε:     ")
        if choice == "1":
            return "shop"
        elif choice == "2":
            return "tavern"
        elif choice == "3":
            return "forest"

class Shop(Scene):
    def start(self,player):
        print("*"*50)
        print("--ΜΑΓΑΖΙ--")
        print("*"*50)
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
    print("*"*50)
    print("--ΤΑΒΕΡΝΑ--")   
    print("*"*50)
    print("Καλωσορισες στην ταβερνα, τι θελεις να κανεις;")
    print("1. Μιλα με τον ιδιοκτητη")  
    print("2. Μιλα με τους πελατες")
    print("3. Φύγε") 

class Forest(Scene):
   
    def start(self,player):
        
        if not self.is_fight_finished:
            print("*"*50)
            print("--ΔΑΣΟΣ--")
            print("")
            print("*"*50)
            player.change_scene("forest")
            print("Ξαφνικα ενα πρασινο γκομπλιν πεφτει απο ενα δεντρο, εισαι αρκετα δυνατος για να το αντιμετωπισεις?!")
            print("1. Μάχη")
            print("2. Φύγε")
            choice = input("Επέλεξε:     ")
            if choice == "1":
                enemy = Goblin()
                combat = Combat(player, enemy)
                result = combat.start_battle()
                if result == "victory":
                    self.is_fight_finished = True
                    
            
                elif result == "defeat":
                    print("Πεθανες πατα enter για να επιστρεψεις στο χωριο")
                    input("Press enter to continue")
                    return "village"
            
            if self.is_fight_finished:
                print("Κερδιζοντας το αγριο goblin βρισκεις ενα κλειδι ")
                print("\n1. Παιρνεις το κλειδι \n2. Γυρνας στο χωριο")
                choice = input()
                while choice != "1" or choice != "2":
                    print("Πρεπει να διαλεξεις σε '1' η '2'")
                    choice = input("\n1. Παιρνεις το κλειδι \n2. Γυρνας στο χωριο")
                    if choice == "1":
                        return "cave"
                    else:
                        return "village"
                
class Cave(Scene):
    def start(self,player):
        print("*"*50)
        print("--ΣΠΗΛΙΑ--")
        print("")
        print("*"*50)
        player.change_scene("cave")
        print("Εχωντας σκοτωσει το γκομπλιν και εχωντας το κλειδι, βρισκεσαι μπροστα σε μια σπηλιά.")
        print("Θα χρησιμοποιησεις το κλειδι για να την ανοιξεις; ")
        print("1. Ναι")
        print("2. Οχι, γυρνα στο χωριο")
        choice = input("Επέλεξε:     ")
        while choice != "1" or choice != "2":
            print("Πρεπει να διαλεξεις σε '1' η '2'")
            choice = input("Επέλεξε:     ")
            if choice == "1":
                return 'secret_room'
            else:
                return "village"
            
class SecretRoom(Scene):
    def start(self,player):
        print("*"*50)
        print("--ΜΥΣΤΙΚΟ ΔΩΜΑΤΙΟ--")
        print("")
        print("*"*50)
        player.change_scene("secret_room")
        print("Ανοιγοντας την πορτα της σπηλιας, αντικριζεις θησαυρους και μια δυσοιωνη ατμοσφαιρα.")
        if self.is_fight_finished == False:
            print("πλησιαζοντας τον θησαυρο, μια σκοτεινη φιγουρα εμφανιζεται και σε προκαλει σε μαχη.")
            print("Εισαι ικανος για να αντιμετωπισεις τον εχθρο;")
            print("1. Μάχη")
            print("2. Φύγε")
            choice = input("Επέλεξε:     ")
            if choice == "1":
                enemy = Troll()
                combat = Combat(player, enemy)
                result = combat.start_battle()
                if result == "victory":
                    self.is_fight_finished = True
                    print("Κερδισες την μαχη και αποκτησες τον θησαυρο!")
                    return "end"
                elif result == "defeat":
                    print("Πεθανες πατα enter για να επιστρεψεις στο χωριο")
                    input("Press enter to continue")
                    return "village"
                
                if self.is_fight_finished:
                    print("Κερδιζοντας το αγριο troll και βλεπεις ενα μεταγιον γυρο απο το λαιμο του")
                    print("Το παιρνεις;")
                    print("1. Ναι")
                    print("2. Οχι, γυρνα στο χωριο")
                    choice = input("Επέλεξε:     ")
                    while choice != "1" or choice != "2":
                        print("Πρεπει να διαλεξεις σε '1' η '2'")
                        choice = input("Επέλεξε:     ")
                    if choice == "1":
                        print("Παίρνοντας το μεταγιον, νιωθεις μια απιστευτη δυναμη να σε διαπερνα.")
                        print("+20 ποντοι επιθεσης, +20 ποντοι αμυνας, +20 ποντοι υγειας, +20 ποντοι μανα")
                        player.Attack += 20
                        player.Defense += 20
                        player.Health += 20
                        player.Mana += 20
                        return "village"
                    else:
                        return "village"
        else:
            print("Ολοκληρωσες την απστολη και εχεις αποκτησει τον θησαυρο, συγχαρητηρια!")
            print("Γυρνας πισω στο χωριο.")
            return "village"