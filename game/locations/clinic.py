from game import location
from game import config
from game.display import announce
from game.events import *
from game.ship import *
from game.player import *

class Clinic (location.Location):

    def __init__(self, x, y, w):
        super().__init__(x, y, w)
        self.name = "clinic"
        self.symbol = "C"
        self.visitable = True
        self.starting_location = Hospital_on_foot(self)
        self.locations = {}
        self.locations["hospital"] = self.starting_location
        self.locations["front desk"] = FrontDesk(self)
        self.locations["waiting room"] = WaitingRoom(self)
        self.locations["bathroom"] = Bathroom(self)
        self.locations["emergency room"] = EmergencyRoom(self)
        self.locations["food station"] = FoodStation(self)
        self.locations["powder store"] = PowderStore(self)
        #self.locations["medicine"] = Medicine(self)

    def enter (self, ship):
        print("\nThe ship has arrived to a clinic!\n")

    def visit (self):
        config.the_player.location = self.starting_location
        config.the_player.location.enter()
        super().visit()

class Hospital_on_foot (location.SubLocation):
    def __init__(self, m):
        super().__init__(m)
        self.name = "hospital"
        self.verbs["forward"] = self
        self.verbs["backward"] = self
        self.verbs["left"] = self
        self.verbs["right"] = self

    def enter (self):
        print("\nThe ship has been anchored and you have entered the hospital.\n")

    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "backward"):
            #Pirates return to their ship
            print("\nThe pirates have returned to the ship.\n")
            config.the_player.next_loc = config.the_player.ship
            config.the_player.visiting = False
            
        elif (verb == "forward"):
            #Takes pirates to the front desk class
            config.the_player.next_loc = self.main_location.locations["front desk"]

        elif (verb == "right"):
            #Takes pirates to the waiting room
            config.the_player.next_loc = self.main_location.locations["waiting room"]

        elif (verb == "left"):
            #Takes pirates to the bathroom
            config.the_player.next_loc = self.main_location.locations["bathroom"]


class FrontDesk (location.SubLocation):
    def __init__(self, m):
        super().__init__(m)
        self.name = "front desk"
        self.verbs["forward"] = self
        self.verbs["backward"] = self
        self.verbs["leave"] = self


    def enter (self):
        print("\nThe pirates are currently at the front desk.\n")

    def process_verb(self, verb, cmd_list, nouns):
        if (verb == "leave"):
            print("\nThe pirates have returned to the ship.\n")
            config.the_player.next_loc = config.the_player.ship
            config.the_player.visiting = False
            
        elif (verb == "backward"):
            #Pirates go to waiting room
            config.the_player.next_loc = self.main_location.locations["waiting room"]

        elif (verb == "forward"):
            #Pirates are at front desk and will select what help they need
            print("\nHello, I'm Mandy! What do you need help with today?\n")
            print("a - Need the bathroom\nb - About to die\nc - Extremely hungry\nd - Need more powder\ne - In need of medicine\nf - Go back on ship\n")
            feedback = input()

            if feedback == "a":
                #Pirates will go to bathroom
                config.the_player.next_loc = self.main_location.locations["bathroom"]

            elif feedback == "b":
                #Pirates will go to emergency room
                config.the_player.next_loc = self.main_location.locations["emergency room"]

            elif feedback == "c":
                #Pirates will go to food station
                config.the_player.next_loc = self.main_location.locations["food station"]

            elif feedback == "d":
                #Pirates will go to powder store
                config.the_player.next_loc = self.main_location.locations["powder store"]

            elif feedback == "e":
                #Pirates will go to get medicine
                config.the_player.next_loc = self.main_location.locations["medicine"]

            elif feedback == "f":
                print("\nThe pirates have returned to your ship.\n")
                config.the_player.next_loc = config.the_player.ship
                config.the_player.visiting = False

class WaitingRoom(location.SubLocation):
    def __init__(self, m):
        super().__init__(m)
        self.name = "waiting room"
        self.verbs["sit"] = self
        self.verbs["sleep"] = self


    def enter(self):
        print("\nThe pirates have now stepped into the waiting room.\n")

    def process_verb(self, verb, cmd_list, nouns):
        if (verb == "sit"):
            #Pirates sit in the waiting room, relaxing a little which earns them some health points
            print("\nThe pirates are sitting down and resting a little.\n")
            c = config.the_player.get_pirates()
            for crewmate in c: 
                crewmate.add_health(10)
            config.the_player.next_loc = self.main_location.locations["front desk"]
            print("\nThe pirates are leaving the room.\n")

            #Ask pirates if they want to access different locations or if they are ready to leave

        elif (verb == "sleep"):
            #Pirates sleep in the waiting room earning a lot more health points
            print("\nThe pirates are taking a nap and resting their exhausted bodies\n")
            c = config.the_player.get_pirates()
            for crewmate in c: 
                crewmate.add_health(20)
            config.the_player.next_loc = self.main_location.locations["front desk"]
            print("\nThe pirates are leaving the room.\n")

            #Ask pirates if they want to access different locations or if they are ready to leave

class Bathroom(location.SubLocation):
    def __init__(self, m):
        super().__init__(m)
        self.name = "bathroom"
        self.verbs["urinate"] = self
        self.verbs["wash"] = self


    def enter(self):
        print("\nThe pirates are currently in the bathroom.\n")

    def process_verb(self, verb, cmd_list, nouns):
        if (verb == "urinate"):
            print("\nThe pirates emptied out their bladders in the toilet and feel relieved.\n")
            c = config.the_player.get_pirates()
            for crewmate in c:
                crewmate.add_health(15)
            config.the_player.next_loc = self.main_location.locations["front desk"]
            print("\nThe pirates are leaving the room.\n")

        elif (verb == "wash"):
            print("\nThe pirates washed their hands in the sink and lessened their chances of getting diseases.\n")
            c = config.the_player.get_pirates()
            for crewmate in c:
                crewmate.add_health(5)
            config.the_player.next_loc = self.main_location.locations["front desk"]
            print("\nThe pirates are leaving the room.\n")
            

class EmergencyRoom(location.SubLocation):
    def __init__(self, m):
        super().__init__(m)
        self.name = "emergency room"
        self.verbs["heal"] = self

    def enter(self):
        print("\nThe pirates are in the emergency room.\n")

    def process_verb(self, verb, cmd_list, nouns):
        if (verb == "heal"):
            print("\n The pirates are receiving extreme care to bounce back healthier than ever.\n")
            c = config.the_player.get_pirates()
            for crewmate in c:
                crewmate.add_health(50)
            config.the_player.next_loc = self.main_location.locations["front desk"]
            

class FoodStation(location.SubLocation):
    def __init__(self, m):
        super().__init__(m)
        self.name = "food station"
        self.verbs["eat"] = self
        self.verbs["take"] = self

    def enter(self):
        print("\nThe pirates are at the food station.\n")

    def process_verb(self, verb, cmd_list, nouns):
        if (verb == "eat"):
            print("\nThe pirates are eating and gaining strength back\n")
            c = config.the_player.get_pirates()
            for crewmate in c:
                crewmate.add_health(10)
            config.the_player.next_loc = self.main_location.locations["front desk"]
            print("\nThe pirates are leaving the room.\n")
        elif (verb == "take"):
            print("\nThe pirates are collecting food to take back to the ship.\n")
            config.the_player.ship.add_food(17)
            print("\nThe pirates are leaving the room.\n")
            config.the_player.next_loc = self.main_location.locations["front desk"]
            
        

class PowderStore(location.SubLocation):
    def __init__(self, m):
        super().__init__(m)
        self.name = "powder store"
        self.verbs["restock"] = self

    def enter(self):
        print("\nThe pirates are at the powder restock room.\n")
        
    def process_verb(self, verb, cmd_list, nouns):
        #The pirates are checking if the powder is in need of restocking and restocking it if necessary
        if(verb == "restock"):
            print("\nThe pirates are restocking the powder if needed.\n")
            c = config.the_player.get_pirates()
            for crewmate in c:
                crewmate.restock()
            print("\nThe pirates are leaving the room.\n")
            config.the_player.next_loc = self.main_location.locations["front desk"]

##class Medicine(location.Sublocation):
##    def __init__(self, m):
##        super().__init__(m)




















        
                
                

