from flashtext.keyword import KeywordProcessor
class TextParseUniversal:
    """
    Text Parse Class creates a text parsing object; initialized with a list of strings that
    will be referenced when using TextParse attributes
    """

    def __init__(self, stringList:list, isCaseSensitive:bool):
        """
        Initializes TextParse object with a list of strings, and if parser should be
        case sensitive as object attributes
        """
        self.stringList = stringList
        self.isCaseSensitive = isCaseSensitive
        self.setNormalizedList()
        self.processor = KeywordProcessor()
        self.setKeywords()


    def __repr__(self):
        """
        Representation of the TextParse object with indication of being case sensitive
        """
        case = "IS NOT"
        if self.isCaseSensitive:
            case = "IS"
        return f"This is a TextParse object that parses text with reference to initialized list and {case} case sensitive."


    """
    Class Setters
    """
    def setNormalizedList(self):
        """
        Class setter which normalizes list of strings; turns all words in list
        to lowercase to represent case sensitivity
        """
        if self.isCaseSensitive:
            self.stringList = [word.lower() for word in self.stringList]
        else:
            pass
    def setKeywords(self):
        """
        Class setter which adds all keywords in self.stringList into self.processor
        """
        self.processor.add_keywords_from_list(self.stringList)


    """
    Class Parsing Methods
    """
    def stringDoesExist(self, string:str) -> bool:
        """
        TextParse method that splits a string into words and
        returns True bool if n > 0 words exist in self.stringList
        """
        keysFound = self.processor.extract_keywords(string)
        return bool(keysFound)

    def listKeywords(self, string:str) -> list:
        """
        TextParse method that returns a list of all words in a given
        string that exist in self.stringList
        """
        if self.stringDoesExist(string):
            return self.processor.extract_keywords(string)
        else:
            return None

    def getFirstKeyword(self, string:str) -> str:
        """
        TextParse method that returns the first instance of a keyword
        that exists within given string
        """
        if self.stringDoesExist(string):
            return self.listKeywords(string)[0]
        else:
            return None
