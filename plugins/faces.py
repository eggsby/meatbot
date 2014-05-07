from util import hook, http
from random import choice

@hook.command(autohelp=False)
def face(inp):
    url = "http://smiley.meatcub.es:1337/api/v1"

    if inp == "help":
        return ".face [ <tag>|tags ] - get an emoticon - thx https://github.com/kid-icarus/lysergix-api" 

    if inp == "tags":
        return ", ".join(http.get_json("%s/tags" % url))

    if inp:
        return http.get_json("%s/random/%s" % (url, inp)).get('content', 'whoops')

    return http.get_json("%s/random" % url).get('content', 'oops')
