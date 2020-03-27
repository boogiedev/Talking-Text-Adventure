import random
class NPC:
    """
    NPC Class that creates an NPC object that interacts with user through keyword dependent response
    """
    def __init__(self, name:str, keyToResponse:dict, randomResponseList:list) -> None:
        """
        Initializes NPC instance with NPC name, sets bool based on if NPC is character "Jabberwordy"
        """
        self.name = name
        self.keyToResponse = keyToResponse
        self.randomResponseList = randomResponseList

    def __repr__(self):
        return f"               It looks like {self.name} lives around here..."
    """
    Class Getters
    """
    def getName(self) -> str:
        """
        Class getter that returns NPC name
        """
        return self.name.title()
    def getTalkResponse(self, key:str="") -> str:
        """
        Class method that takes in user string, keyword to return a randomized appropriate response from self.keyToResponse dictionary
        """
        if self.isValidKey(key):
            responseCat = self.keyToResponse[key]
            i = random.randint(0, len(responseCat) - 1)
            return responseCat[i]
        else:
            return self.getRandomResponse()
            # return "Mmmmmm I don\'t really know what you\'re saying..."
    def getRandomResponse(self) -> str:
        i = random.randint(0, len(self.randomResponseList)- 1)
        return self.randomResponseList[i]

    def isValidKey(self, key:str) -> bool:
        try:
            self.keyToResponse[key]
            return True
        except:
            return False


#




























        #
