"""
Game words for parsing and use specific to TTA
"""

# NPC NAMES
jabberwordy = "Jabberwordy"

npcNames = ["Isabelle", "Slider", "Gracie", "Wisp", "Tex", "Nook", "Poppy"]


# NPC RESPONSES
"""HELLO/HI"""
hello = [
"It is wonderful to meet you.",
"Oh. Hey there.",
"Hi yourself, stranger.",
"Um…hello.",
"Didn’t I already say hello?",
"Hello. Goodbye. It’s all the same.",
"I think this is the first of many greeting we’ll share.",
"Greetings my new friend!",
"Bonjour, hola, guten tag, ciao, namaste, salaam. Oh….and hello, my friend."
]
"""LOVE"""
love = [
"It is wonderful to meet you.",
"Oh. Hey there.",
"Hi yourself, stranger.",
"Um…hello.",
"Didn’t I already say hello?",
"Hello. Goodbye. It’s all the same.",
"I think this is the first of many greeting we’ll share.",
"Greetings my new friend!",
"Bonjour, hola, guten tag, ciao, namaste, salaam. Oh….and hello, my friend."
]
"""BEATIFUL"""
beautiful = [
"It is wonderful to meet you.",
"Oh. Hey there.",
"Hi yourself, stranger.",
"Um…hello.",
"Didn’t I already say hello?",
"Hello. Goodbye. It’s all the same.",
"I think this is the first of many greeting we’ll share.",
"Greetings my new friend!",
"Bonjour, hola, guten tag, ciao, namaste, salaam. Oh….and hello, my friend."
]
"""WEATHER"""
weather = [
"It is wonderful to meet you.",
"Oh. Hey there.",
"Hi yourself, stranger.",
"Um…hello.",
"Didn’t I already say hello?",
"Hello. Goodbye. It’s all the same.",
"I think this is the first of many greeting we’ll share.",
"Greetings my new friend!",
"Bonjour, hola, guten tag, ciao, namaste, salaam. Oh….and hello, my friend."
]
"""NAME"""
name = [
"It is wonderful to meet you.",
"Oh. Hey there.",
"Hi yourself, stranger.",
"Um…hello.",
"Didn’t I already say hello?",
"Hello. Goodbye. It’s all the same.",
"I think this is the first of many greeting we’ll share.",
"Greetings my new friend!",
"Bonjour, hola, guten tag, ciao, namaste, salaam. Oh….and hello, my friend."
]


npcResponses = {"love":love, "beautiful":beautiful, "hello":hello, "hi":hello, "name":name, "weather":weather}
npcRandomResponses = [
"Wahooo! I'm all done with work! Now I'm free!",
"Mmmmmm I don\'t really know what you\'re saying...",
"WAHOOOOOOO! All the cockroaches are gone! Now everything is all better!",
"Check it out! I found a four-leaf clover! Does this mean I'll be really lucky now?",
"Itchy itchy itchy! I got bit by a mosquito..." ,

]


USERCOMMANDS = ['look', 'help', 'map', 'up', 'down', 'left', 'right']
userCmdDict = {"cmd":['look', 'help', 'map'], "move":['up', 'down', 'left', 'right']}
TALKKEYS = ["love", "beautiful", "hello", "hi", "name", "weather"]

WRONGCOMMAND = """
        I don\' think that\'s a command. . . pretty sure
        Or maybe it's not specific enough... try "help"
"""

WRONGONETWO = """
        I don\' think that\'s a command. . . pretty sure
        Maybe try just entering either "1" or "2" or "quit" (to exit)
"""



HELPDOC = display_profile = f"""
|===========================================================================|
| CMD     | KEYWORD |  DETAIL                                               |
|===========================================================================|
| LOOK    | "LOOK"  | GIVES EXPLAINATION OF THE CURRENT AREA USER IS IN     |
| HELP    | "HELP"  | LISTS AVALIABLE COMMAND KEYWORDS..AS IN LIKE RIGHT NOW|
| MAP     | "MAP"   | DISPLAYS VISUAL MAP WITH "X" DENOTING USER POSITION   |
|===========================================================================|
|===========================================================================|
| MOVEMENT | KEYWORD(S) |  DETAIL                                           |
|===========================================================================|
| UP       | "UP"       | THIS MOVES YOU UP                                 |
| DOWN     | "DOWN"     | OH! THIS MOVES YOU... DOWN!                       |
| LEFT     | "LEFT"     | NOT SURE WHY YOU'RE STILL READING THIS...         |
| RIGHT    | "RIGHT"    | *REFER TO ANECDOTE BELOW IF YOU'RE STILL READING  |
|===========================================================================|


* Tʜᴇʀᴇ ᴀʀᴇ ᴛᴡᴏ ᴛʏᴘᴇs ᴏғ ᴘᴇᴏᴘʟᴇ ɪɴ ᴛʜᴇ ᴡᴏʀʟᴅ:
1. Tʜᴏsᴇ ᴡʜᴏ ᴄᴀɴ ᴇxᴛʀᴀᴘᴏʟᴀᴛᴇ ғʀᴏᴍ ɪɴᴄᴏᴍᴘʟᴇᴛᴇ ᴅᴀᴛᴀ sᴇᴛs.

"""



movementDict = {'left':lambda x: (x[0], x[1] - 1), 'right':lambda x: (x[0], x[1] + 1), 'up':lambda x: (x[0] - 1, x[1]), 'down':lambda x: (x[0] + 1, x[1])}
moveUpDiag = """
                        You moved %s
"""

# JABBER DPROMPT
#DPROMPT%("the",npc)
# ELSE
#DPROMPT%("",npc)
DPROMPT = """
You can say something to %s %s. . .
"""

# JABBER DIALOGUE
#DIALOGUE%(x,npc,y,"the", npc)
# ELSE
#DIALOGUE%(x,npc,y,"", npc)
DIALOGUE = """
        You: %s
        %s: %s

Options:
Type something to talk to%s %s! Or type "quit" to leave.

"""
