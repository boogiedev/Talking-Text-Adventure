class Item:
    def __init__(self, name:str, description:str, category:str, isConsumable:bool) -> None:
        self.name = name
        self.description = description
        self.category = category
        self.isConsumable = isConsumable
        self.data = self.buildData()
    def __repr__(self) -> str:
        return f"This is a(n) {self.name}"
    def __call__(self):
        return self.name
    """
    Class Getters
    """
    def getName(self):
        return self.data[0]
    def getDescription(self):
        return self.data[1]
    def getCategory(self):
        return self.data[2]
    def getConsumability(self):
        return self.data[3]
    def getData(self):
        return self.data



    """
    Class Methods
    """
    def buildData(self):
        return [self.name, self.description, self.category, self.isConsumable]
