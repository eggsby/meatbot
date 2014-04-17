from random import randint
from util import hook

@hook.command(autohelp=False)
def dongues(inp):
    berries = 3 if randint(0, 1) else 8
    shaft = '=' * randint(5, 20)
    return "%s%sD ~ ~ ~ %s" % (berries, shaft, inp)
