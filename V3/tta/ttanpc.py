from npc import *
from ttainventory import *
from ttagamedata import *
class TTANpc(NPC):
    def __init__(self, name:str="TTA Default NPC", keyToResponse:dict=npcResponses, randomResponseList:list=npcRandomResponses):
        self.name = name
        self.keyToResponse = keyToResponse
        self.randomResponseList = randomResponseList
        self.isJabberwordy = False
        self.inventory = TTAInventory(self.name)

class Jabberwordy(NPC):

    DEFAULTRESPONSE = "I think you talk weird"
    # JABBER RESPONSE
    jWords = [
    'allocution', 'ancient', 'antidisestablishmentarianism', 'autonomy', 'ballerina', 'banana', 'bankroll', 'berserker', 'birthplace', 'blathering', 'blister', 'bouncy', 'boutique', 'candelabra', 'cannibal', 'capacitor', 'catalyst', 'chandelier', 'chauffer', 'circuit', 'conundrum', 'craven', 'creepy', 'crustaceous', 'dance', 'dangerous', 'daring', 'dastardly', 'delude', 'download', 'dragon', 'ego', 'emphysema', 'ephemeral', 'etui', 'evaluate', 'feudal', 'fiery', 'flabbergasted', 'flux', 'forsooth', 'frothing', 'fudgesickle', 'funky', 'galloping', 'ghostly', 'glassy', 'gold', 'gooseneck', 'grizzly', 'grok', 'grommet', 'hashing', 'hibernation', 'Hogwarts', 'impure', 'incandescent', 'incubus', 'jump', 'limerick', 'melodrama', 'monger', 'monotone', 'muscle', 'obelisk', 'omnivore', 'ostensibly', 'pantaloons', 'papaya', 'parasite', 'patronus', 'pectoral', 'plebian', 'portcullis', 'punch', 'reagent', 'referee', 'salamander', 'savage', 'scalawag', 'serendipitous', 'seventeen', 'shameful', 'shanty', 'slither', 'sonic', 'spaceship', 'spongey', 'square', 'succubus', 'tango', 'tape', 'toaster', 'toothy', 'twine', 'volcano'
    ]
    # USER KEYWORDS
    userComWords = [
    'above', 'across', 'add', 'adventure', 'also', 'are', 'bad', 'because', 'below', 'but', 'by', 'can', 'crazy', 'day', 'direction', 'for', 'from', 'funny', 'go', 'good', 'have', 'how', 'if', 'java', 'just', 'keep', 'most', 'move', 'need', 'no', 'other', 'people', 'program', 'same', 'some', 'speak', 'speech', 'strange', 'subtract', 'talk', 'text', 'them', 'then', 'there', 'they', 'think', 'this', 'way', 'what', 'where', 'who', 'why', 'with', 'word', 'yes', 'you'
    ]
    def __init__(self, name:str="Jabberwordy"):
        self.name = name
        self.isJabberwordy = True
        self.keyToResponse = None
        self.inventory = TTAInventory(self.name)

    def getTalkResponse(self, string:str="") -> str:
        """
        Class method that takes a user talking string and converts all "common" words (from game_words) in string and returns randomized "Jabberwordy" reponse
        """
        jabberResponse = []
        if not string.strip():
            string = self.DEFAULTRESPONSE
        for word in string.split():
            i = random.randint(0, len(self.jWords)-1)
            if word not in self.userComWords:
                jabberResponse.append(word)
            else:
                jabberResponse.append(self.jWords[i])
        return " ".join(jabberResponse) + "."
