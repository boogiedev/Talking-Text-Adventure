from user import User
from ttainventory import *
class TTAUser(User):
    def __init__(self, name="Default User"):
        self.name = name
        self.inventory = TTAInventory(self.name)
