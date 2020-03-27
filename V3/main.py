import sys
sys.path.append('universal')
sys.path.append('tta')
from textparse import *
from ttaModClass import *
from map import *
from visuals import *


"""VISUALS OBJECT"""
visuals = Visuals()
"VISUAL CLASS FUNCS"
dprint = visuals.delay_print
clear = visuals.clear

"""PARSE OBJECT"""
ttaParser = TextParseUniversal(USERCOMMANDS,False)
convoParser = TextParseUniversal(TALKKEYS, False)
"PARSE CLASS FUNCTIONS"
getkey = ttaParser.getFirstKeyword
getTalk = convoParser.getFirstKeyword

"PARSE GAME FUNCTIONS"
def FINDEXECUTECOMMAND(keyword:str) -> None:
    isMove = lambda x: x in userCmdDict["move"]
    if isMove(keyword):
        doMove(keyword)
    else:
        doCommand(keyword)

def doCommand(key:str) -> None:
    if key == "look":
        look()
    elif key == "help":
        print(HELPDOC)
    elif key == "map":
        print()
        x = getUSERCORD()
        updateMap(x, USERSYMB)
        print(getMap())

def doMove(key:str) -> None:
    changeCord(key)
    x = getUSERCORD()
    updateMap(x, USERSYMB)

def look() -> None:
    print()
    occupant = getOccupant()
    location = locDescripDict[occupant]
    print(areaDescription)
    print(location)

"PARSE GAME FUNCTIONS"

# CHANGES FINAL COORDINATE DOES NOT CHECK KEY
def changeCord(key:str) -> None:
    curCord = getUSERCORD()
    modCord = movementDict[key](curCord)
    if checkSymVal(modCord):
        CHANGECORD(modCord)
        i = "\'" + key + "\'"
        print(moveUpDiag%i)
# CHECKS SYMBOL THEN COORDINATE
def checkSymVal(cord:tuple=(1,1),sym:str="X") -> bool:
    if isValSym(sym):
        if isValMove(cord):
            return True
    else:
        print("If this message prints out... that means you broke the game")
        return False

"""MAP INIT"""
ttaMap = GameMap(3)
"MAP FUNCS"
getMap = ttaMap.getVisual
getCord = ttaMap.getCoordinates
cordList = ttaMap.getCoordinatesList()
updateMap = ttaMap.updateMap
# VALIDATORS
isValSym = ttaMap.isValidSymbol
isValMove = ttaMap.isValidMove

"""NPC TESTS"""
"JABBERWORDY INIT"
# jabberwordy = Jabberwordy()
"CHIVES INIT"
# chives = TTANpc("Chives")
"TTA NPC INIT"
ttaNPCNames = npcNames
npcDict = dict(zip(ttaNPCNames, [TTANpc(char) for char in ttaNPCNames]))
npcDict[jabberwordy] = Jabberwordy()
ttaNPCNames.append("Jabberwordy")
npcDict["Chives"] = TTANpc("Chives",chivesDict, chivesRandomResponseList)
ttaNPCNames.append("Chives")

"MAP NPC TO CORD"
# Shuffles NPC List
random.shuffle(ttaNPCNames)
# GLOBAL CORDtoNPC DICT
NPCLOCATIONDICT = dict(zip(cordList, ttaNPCNames))

"""GAME SPECIFIC FUNCTIONS"""

'CONVERSATION FUNCTIONS'
awkSilence = lambda x: not bool(x)
# Conversaion INIT with npc
def initiateConvo() -> None:
    cord = getUSERCORD()
    npc = getOccupant()
    npcObj = npcDict[npc]
    if npcObj.isJabberwordy:
        jabberConvo()
    else:
        normalConvo(npc,npcObj)

def jabberConvo(npc:name="Jabberwordy", npcObj:object=npcDict["Jabberwordy"]) -> None:
    print(DPROMPT%("the",npc))
    x = input()
    while x != "quit":
        if awkSilence(x):
            y = npcObj.getTalkResponse(x)
            x = ". . . . ."
        else:
            y = npcObj.getTalkResponse(x)
        print(DIALOGUE%(x,npc,y," the", npc))
        x = input()

def normalConvo(npc:name, npcObj:object) -> None:
    print(DPROMPT%("",npc))
    x = input()
    while x != "quit":
        key = getTalk(x)
        if awkSilence(x):
            x = ". . . . ."
            y = npcObj.getRandomResponse()
        else:
            y = npcObj.getTalkResponse(key)
        print(DIALOGUE%(x,npc,y,"", npc))
        x = input()

def getOccupant() -> str:
    cord = getUSERCORD()
    return NPCLOCATIONDICT[cord]

"USER 1 2 INPUT VALIDATION"
def getOneTwoCmd(prompt:str) -> int:
    print(prompt)
    x = input()
    valid = ["1", "2", "quit"]
    while x not in valid:
        print(WRONGONETWO)
        print(prompt)
        x = input()
    if x == "1":
        return "1"
    elif x == "2":
        return "2"
    elif x == "quit":
        return "quit"


" MAIN GAME LOOP "
# MAIN OPTION LOOP THAT IS EITHER 1, 2, CMD, or QUIT
# 1 MOVES USER TO NEXT ACTION
# 2 MOVES USER BACK TO MAIN OPTION LOOP AND PRINTS RELAVENT INFORMATION
# CMD MOVES USER TO COMMAND LOOP
# QUIT LETS USER EXIT GAME
def mainOPSLOOP() -> None:
    valid = ["1", "2"]
    print(PROMPT1)
    x = input()
    while x != "quit":
        keyword = getkey(x)
        if keyword:
            FINDEXECUTECOMMAND(keyword)
        elif x == "1":
            occupant = npcDict[getOccupant()]
            look()
            print()
            print(occupant)
            y = getOneTwoCmd(PROMPT2)
            if y == "1":
                initiateConvo()
            else:
                pass
        elif x == "2":
            print(HELPDOC)
        else:
            print(WRONGCOMMAND)
        print(PROMPT1)
        x = input()
    print(THANKSFORVISITING)

if __name__ == "__main__":
    print(title)
    """USER INIT"""
    USERNAME = input(userNamePrompt)
    # CREATES USER OBJECT
    ttaUser = TTAUser(USERNAME)
    # ASSIGN DEFAULT COORDINATE
    ttaUser.assignMisc((1,1))
    # ASSIGN DEFAULT SYMBOL
    USERSYMB = "X"
    # USER FUNCS
    CHANGECORD = ttaUser.assignMisc
    getUSERCORD = ttaUser.getMisc
    # USERCORD MAP INIT

    print(INTRODUCTIONa)
    mainOPSLOOP()
