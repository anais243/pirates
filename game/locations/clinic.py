from game import location
from game import config
from game.display import announce
from game.events import *

class Clinic (location.Location):

    def __init__(self, x, y, w):
        super().__init__(x, y, w)
        self.name = "clinic"
        self.symbol = "C"
        self.visitable = True
        self.starting_location = Beach_with_ship(self)
        self.locations = {}
        self.locations["hospital"] = self.starting_location
        self.locations["front desk"] = FrontDesk(self)
        self.locations["waiting room"] = WaitingRoom(self)
        self.locations["bathroom"] = Bathroom(self)
        self.locations["emergency room"] = EmergencyRoom(self)
        self.locations["food station"] = FoodStation(self)
        self.locations["powder store"] = PowderStore(self)
        self.locations["medicine"] = Medicine(self)

        def enter (self, ship):
            print("The ship has arrived to a clinic!")

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
            print("The ship has been anchored and you have entered the hospital.")

        def process_verb (self, verb, cmd_list, nouns):
            if (verb == "backward"):
                #Pirates return to their ship
                print("You have returned to your ship.")
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


class FrontDesk (location.Sublocation):
    def __init__(self, m):
        super().__init__(m)
        self.name = "front desk"
        self.verbs["forward"] = self
        self.verbs["backward"] = self


    def enter (self):
        print("The pirates are currently at the front desk.")

    def process_verb(self, verb, cmd_list, nouns):
        if (verb == "backward"):
            #Pirates go to waiting room
            config.the_player.next_loc = self.main_location.locations["waiting room"]

        elif (verb == "forward"):
            #Pirates are at front desk and will select what help they need
            print("Hello, I'm Mandy! What do you need help with today?")
            print("a - Need the bathroom\nb - About to die\nc - Extremely hungry\nd - Need more powder\ne - In need of medicine\n")
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

class WaitngRoom(location.Sublocation):
    def __init__(self, m):
        super().__init__(m)
        self.name = "waiting room"
        self.verbs["sit"] = self
        self.verbs["sleep"] = self


    def enter(self):
        print("The pirates have now stepped into the waiting room.")

    def process_verb(self, verb, cmd_list, nouns):
        if (verb == "sit"):
            #Pirates sit in the waiting room, relaxing a little which earns them some health points
            c = config.the_player.get_pirates()
            for crewmate in c: 
                crewmate.add_health(10)

            #Ask pirates if they want to access different locations or if they are ready to leave

        elif (verb == "sleep"):
            #Pirates sleep in the waiting room earning a lot more health points
            c = config.the_player.get_pirates()
            for crewmate in c: 
                crewmate.add_health(20)

            #Ask pirates if they want to access different locations or if they are ready to leave

class Bathroom(location.Sublocation):
    def __init__(self, m):
        super().__init__(m)
        self.name = "bathroom"
        self.verbs["urinate"] = self
        self.verbs["wash"] = self


        def enter(self):
            print("The pirates are currently in the bathroom.")

        def process_verb(self, verb, cmd_list, nouns):
            if (verb == "urinate"):
                print("The pirates emptied out their bladders in the toilet and feel relieved.")
                c = config.the_player.get_pirates()
                for crewmate in c:
                    crewmate.add_health(15)

            elif (verb == "wash"):
                print("The pirates washed their hands in the sink and lessened their chances of getting diseases.")
                c = config.the_player.get_pirates()
                for crewmate in c:
                    crewmate.add_health(5)
                

##class EmergencyRoom(location.Sublocation):
##    def __init__(self, m):
##        super().__init__(m)
##        self.name = "emergency room"
##        self.verbs[""]

class FoodStation(location.Sublocation):
    def __init__(self, m):
        super().__init__(m)
        self.name = "food station"
        self.verbs["eat"] = self
        self.verbs["take"] = self

        def enter(self):
            print("The pirates are at the food station.")

        def process_verb(self, verb, cmd_list, nouns):
            if (verb == "eat"):
                print("The pirates are eating and gaining strength back")
                c = config.the_player.get_pirates()
                for crewmate in c:
                    crewmate.add_health(10)
            elif (verb == "take"):
                print("The pirates are collecting food to take back to the ship.")
                c = config.the_player.get_pirates()
                for crewmate in c:
                    ship.add_food(7)
                
        

##class PowderStore(location.Sublocation):
##    def __init__(self, m):
##        super().__init__(m)
##
##class Medicine(location.Sublocation):
##    def __init__(self, m):
##        super().__init__(m)




















        
                
                

