import random
from util import hook
import re

sayings = [
":D",
"hi!",
"weed",
"gotta love me!",
"guess who has a boner",
"~*~ sends meat heart <3 <3 <3 ~*~",
"wuts all this commotion about",
"tell me about the rabbits george",
"weeeeeeed",
"en tu ano",
"i'm twerking at tha pyramid 2nite",
"meeeeaaat",
"meat?",
"huehuheuhuehuehue",
"~*aw u kno u luv me <3 xoxo <3*~"
"please direct all questions/comments to @tec27!"
]

@hook.regex(*("(\\bmeat\\b|\\bmeatbot\\b)", re.I))
def meatbotname(inp):
    return random.choice(sayings)

@hook.regex(*("(\\bwow\\b|\\bmom\\b)", re.I))
def wowmom(inp):
    return random.choice(["mom wow", "wow mom"])
