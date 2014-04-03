from util import hook

@hook.command
def fs(inp):
    ".fs <chan> -- get a url to a facespace chan"

    return "https://facespac.es/c/%s" % inp
