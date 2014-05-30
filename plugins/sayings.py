import random
from util import hook
import re

sayings = [
    ":D",
    "weed",
    "gotta love me!",
    "~*~ sends meat heart <3 <3 <3 ~*~",
    "wuts all this commotion about",
    "tell me about the rabbits george",
    "weeeeeeed",
    "en tu ano",
    "i'll c u at tha pyramid 2nite",
    "meeeeaaat",
    "~*aw u kno u luv me <3 xoxo <3*~",
    "meat?",
    "thats kewl.. but how do you feel about ppt?",
    "huehuheuhuehuehue",
    "no boggie",
    "ᕕ( ᐛ )ᕗ  hay",
    "please direct all questions/comments to tec27!",
    "don't talk about balls around tec27!!!"
]

h8r_sayings = [
    "shut up meat 8=========D~~",
    "~*aw u kno u luv me <3 xoxo <3*~"
]

h8rs = [
]

@hook.regex(*("(\\bmeat\\b|\\bmeatbot\\b)", re.I))
def meatbotname(inp, nick=''):
    if nick.lower() in h8rs:
        return random.choice(h8r_sayings)
    return random.choice(sayings)

@hook.regex(*("(\\bwow\\b|\\bmom\\b)", re.I))
def wowmom(inp):
    return random.choice(["mom wow", "wow mom"])

@hook.regex(*("(\\bnot all\\b)", re.I))
def notall(inp, nick=''):
    if nick.lower().endswith('s'):
        return 'NOT ALL ' + nick.upper() + '\'S'
    return 'NOT ALL ' + nick.upper() + 'S'
