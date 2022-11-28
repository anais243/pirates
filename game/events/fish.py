from game import event
from game.ship import *
from game.player import Player
from game.context import Context
import game.config as config
import random

class Fish (Context, event.Event):

    def __init__(self):
        super().__init__()
        self.name = "fish visitor"
        self.fish = 1
        self.verbs['ignore'] = self
        self.verbs['feed'] = self
        self.verbs['catch'] = self
        self.result = {}
        self.go = False

    def process_verb(self, verb, cmd_list, nouns):
        if (verb == "ignore"):
            self.go = True
            r = random.randint(1,10)
            if (r < 5):
                self.result["message"] = "The fish is swimming away. There goes your chance for food."
                if (self.fish > 1):
                    self.fish = self.fish - 1
            else:
                c = random.choice(config.the_player.get_pirates())
                if (c.lucky == True):
                    self.result["message"] = "The fish swam away :("
                else:
                    self.result["message"] = c.get_name() + " is attacked by an angry fish"
                    if (c.inflict_damage (self.fish, "Mauled to death by fish")):
                        self.result["message"] = ".. " + c.get_name() + " is eaten alive by hungry fish!"

        elif (verb == "feed"):
            self.fish = self.fish + 1
            self.result ["newevents"].append (Fish())
            self.result["message"] = "The fish have never felt better. They thank you."
            self.go = True

        elif (verb == "catch"):
            food = input("You have caught the fish! Would you like to keep the fish and fry it for dinner (enter keep) or set it free into the water (enter free)?\n")
            if food == "keep":
                c = random.choice(config.the_player.get_pirates())
                self.result["message"] = c.get_name() + " brought back fish to his crew!"
                c.lucky = True
                config.the_player.ship.add_food(5)
                self.result["newevents"] = [ self ]
                self.go = True

            elif food == "free":
                c = random.choice(config.the_player.get_pirates())
                self.result["message"] = c.get_name() + " decided to let the fish return back to its home."
                self.result["newevents"] = [ self ]
                self.go = True

        else:
            print("It seems the only options here are to ignore, feed, catch, or fry")
            self.go = False


    def process (self, world):

        self.go = False
        self.result = {}
        self.result["newevents"] = [ self ]
        self.result["message"] = "default message"

        while (self.go == False):
            print ("It looks like there is " + str (self.fish) + " fish nearby. What do you want to do?")
            Player.get_interaction ([self])

        return self.result
                  
