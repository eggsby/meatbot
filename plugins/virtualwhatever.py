from util import hook
from twitter import *
from random import randint

messages = [
  "wow great job",
  "en tu ano",
  "huehuehuehue",
  "so gud",
  "yr tweet is my command",
  "SENDIN THAT TWEET 2 THA PYRAMID 2NITE",
  "uh huh",
  "how do you come up with this stuff",
  "BOOM thought leader"
]

def get_message():
    index = randint(1, len(messages)) - 1
    return messages[index]

@hook.api_key('virtualwhatever')
@hook.command('vw')
@hook.command
def virtualwhatever(inp, api_key=None):
    '.virtualwhatever <tweet> -- become a thought leader'

    if not isinstance(api_key, dict) or any(key not in api_key for key in
                                            ('consumer', 'consumer_secret', 'access', 'access_secret')):
        return "error: api keys not set"

    access = api_key.get('access')
    access_secret = api_key.get('access_secret')
    consumer = api_key.get('consumer')
    consumer_secret = api_key.get('consumer_secret')

    twitter = Twitter(auth=OAuth(access, access_secret, consumer, consumer_secret))
    twitter.statuses.update(status=inp)
    tweet = twitter.statuses.user_timeline(screen_name='virtualwhatever')[0]
    return "%s - https://twitter.com/virtualwhatever/status/%s" % (get_message(), tweet.get('id'))
