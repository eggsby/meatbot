from util import hook
from upsidedown import transform

@hook.command
def flip(inp):
    ".flip <something> -- wow mom, life upside down"

    return transform(inp)
