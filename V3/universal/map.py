
class GameMap:
    """
    Map Class that creates a Map object that interacts with user and npc class
    """
    OUTOFBOUNDS = """
        Looks like you\'re about to go out of bounds . . wait . . thats illegal
        Maybe check your map...
"""
    WRONGSYMBOL = """
        9Don't try to blend in with the map...
"""

    def __init__(self, size:int) -> None:
        """
        Initializes the Game Map object and sets map attributes according to arguments passed in
        setSize(default=3 -> 9 Square Map) sets the size of the map with the argument being both length and width of the map
        """
        # MAP ATTRIBUTES
        self.size = size

        # MAP INSTANTIATION
        self.visual = self.buildMapVisual()
        self.coordinateList, self.coordinates = self.buildCoordinates()


        # PLAYER POSITION
        self.position = (1, 1)

    def __repr__(self):
        return f"This is a GameMap object that is {self.size} by {self.size}"

    """
    Class Setters/Constructors (INIT)
    """
    def buildMapVisual(self) -> str:
        """
        Class constructor that creates and returns visual map of game
        """
        size = self.size
        sec1 = lambda n: ("+---" * n) + "+"
        sec2 = lambda n: ("| = " * n) + "|"
        secFull = lambda n: sec1(n) + "\n" + sec2(n) + "\n"
        mapVis = ""
        for _ in range(size):
            mapVis += secFull(size)
        mapVis += sec1(size)
        return mapVis

    def buildCoordinates(self) -> dict:
        """
        Class constructor that creates and returns an array map of game with positions represented by [x, y] coordinates
        """
        n, grid = self.size, []
        for row in range(n):
            for col in range(n):
                tup = (row, col)
                grid.append(tup)
        visPos = [x for x, y in enumerate(self.visual) if y == "="]
        return grid, dict(zip(grid, visPos))
    """
    Class Getters
    """
    def getVisual(self):
        return self.visual
    def getCoordinates(self):
        return self.coordinates
    def getCoordinatesList(self):
        return self.coordinateList
    """
    Class Functions
    """
    def resetMap(self):
        self.visual = self.buildMapVisual()

    def updateMap(self, coordinate:tuple, symbol:str) -> None:
        self.resetMap()
        newMap = ""
        posIdx = self.coordinates[coordinate]
        for i in range(len(self.visual)):
            char = self.visual[i]
            if i != posIdx:
                newMap += char
            else:
                newMap += symbol
        self.visual = newMap

    def isValidMove(self, coordinate:tuple) -> bool:
        try:
            self.coordinates[coordinate]
            return True
        except:
            print(self.OUTOFBOUNDS)
            return False

    def isValidSymbol(self, symbol:str) -> bool:
        if self.visual.count(symbol) <= 1 and len(symbol) == 1:
            return True
        else:
            print(self.WRONGSYMBOL)
            return False


































        #
