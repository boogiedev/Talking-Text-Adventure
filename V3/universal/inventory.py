class Inventory:
    def __init__(self, owner:str) -> None:
        self.owner = owner
        self.items = {}

    def __repr__(self) -> str:
        return f"This is {self.owner}'s inventory"
    """
    Class Getters
    """
    def showItems(self):
        return self.items
    def showSingleItem(self, name:str) -> dict:
        return self.items.get(name, "You don't seem to have this item...")
    """
    Class Resetters
    """
    def resetInventory(self):
        self.items = {}
    """
    Class Methods
    """
    def addItem(self, item:object) -> object:
        name = item()
        self.items[name] = item
    def useItem(self, name:str):
        if self.doesExist(name):
            toUse = self.items.get(name, "")
            if self.isUsable(toUse):
                self.items.pop(item)
            else:
                print("You cant' really use this item...")
                return None
    def removeItem(self, name:str):
        if self.doesExist(name):
            self.items.pop(item)
        else:
            print("You don't even have this??")

    def doesExist(self, name:str) -> bool:
        try:
            self.item[name]
            return True
        except:
            return False



    """
    Class Item Interactions
    """
    def isUsable(self, item):
        try:
            return item.getConsumability()
        except:
            return False
