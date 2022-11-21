from game import event
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
        self.verbs['fry'] = self
        self.result = {}
        self.go = False

    def process_verb(self, verb, cmd_list, nouns):
        if (verb == "ignore"):
            self.result["message"] = "The fish is swimming away. There goes your chance for food."

        elif (verb == "feed"):
            self.fish = self.fish + 1
            self.result ["newevents"].append (Fish())
            self.result["message"] = "The fish have never felt better. They thank you."
            self.go = True

        #elif (verb == "catch"):

        #elif (verb == "fry"):

        else:
            print("It seems the only options here are to ignore, feed, catch, or fry")
            self.go = False

    def process (self, world):

        self.go = False
        self.result = {}
        self.result["newevents"] = [ self ]
        self.result["message"] = "default message"

        while (self.go == False):
            print (str (self.fish) + " it looks like there is fish nearby. What do you want to do?")
            Player.get_interaction ([self])

        return self.result
                  
