from inventory import *
class User:
    """
    User Class that creates an User object that interacts with NPC class
    """

    def __init__(self, name:str) -> None:
        self.name = name
        self.inventory = Inventory(self.name)
        self.misc = None
    """
    Class Getters
    """
    def getName(self) -> str:
        """
        Class getter that returns user's name
        """
        return self.name.title()
    def getMisc(self):
        return self.misc
    """
    Class Methods
    """
    def assignMisc(self, val):
        self.misc = val
