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
"weeeeeeed",
"en tu ano",
"i'm twerking at tha pyramid 2nite",
"meeeeaaat",
"meat?",
"huehuheuhuehuehue"
]

@hook.regex(*("\\bmeat\\b", re.I))
def weedbotname(inp):
    return random.choice(sayings)

@hook.regex(*("\\bwow\\b", re.I))
def wow(inp):
    return "wow mom"

@hook.regex(*("\\bmom\\b", re.I))
def mom(inp):
    return "mom wow"
