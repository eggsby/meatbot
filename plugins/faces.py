from util import hook, http
from random import choice
import re

@hook.command(autohelp=False)
def face(inp):
    url = "http://smiley.meatcub.es:1337/api/v1"
    
    num = re.search('\d+$', inp)
    if num:
        num = int(num.group(0))
        return http.get_json("%s/faces/%s" % (url, num)).get('content', 'whoops')

    if inp == "help":
        return ".face [ < tag | id > | tags ] - get an emoticon - thx https://github.com/kid-icarus/lysergix-api" 

    if inp == "tags":
        return ", ".join(http.get_json("%s/tags" % url))

    if inp:
        return http.get_json("%s/random/%s" % (url, inp)).get('content', 'whoops')

    return http.get_json("%s/random" % url).get('content', 'oops')
