from game import location
from game import config
from game.display import announce
from game.events import *

class CornMaze (location.Location):

    def __init__ (self, x, y, w):
        super().__init__(x, y, w)
        self.name = "cornmaze"
        
            

    
