from random import randint
from util import hook

@hook.command(autohelp=False)
def ding(inp):
    berries = 'ε' if randint(0, 1) else 8
    shaft = '=' * randint(5, 20)
    return "{} ~ ~ ~ ᗡ{}{}".format(inp, shaft, berries)

