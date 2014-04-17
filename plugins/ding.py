from random import randint
from util import hook

@hook.command(autohelp=False)
def ding(inp):
    berries = 3 if randint(0, 1) else 8
    shaft = '=' * randint(5, 20)
    return "%s ~ ~ ~ Ɑ%s%s" % (inp, shaft, berries)
