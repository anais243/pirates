from game import event
import random
import game.config as config

class Healing(event.Event):

    def __init__ (self):
        self.name = " Pirate Crew Healing Camp "

    def process (self, world):
        c = random.choice(config.the_player.get_pirates())
        result = {}
        if (c.sick == True):
            c.set_sickness (True)
            if (c.lucky == True):
                damage = -1
                lifecause = "Has healed from their illness"
            else:
                damage = -10
                lifecause = "Is healing from their severe illness"
            healed = c.inflict_damage (damage, lifecause)
            if(healed == True):
                result["message"] = c.get_name() + " took a turn for the better and is healing from their illness"
                result["newevents"] = [ self, self, self ]
            else:
                result["message"] = c.get_name() + " has taken a turn for the better"
                result["newevents"] = [ self, self ]
        elif (c.lucky == False):
            c.set_sickness (True)
            result["message"] = c.get_name() + " has gotten sick"
            result["newevents"] = [ self, self ]
        else:
            result["message"] = c.get_name() + " felt a bit sick"
            result["newevents"] = [ self ]
        return result
