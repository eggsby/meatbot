from util import hook
from twitter import *
import random

accepted = [
  "wow great job",
  "en tu ano",
  "huehuehuehue",
  "yr tweet is my command",
  "SENDIN THAT TWEET 2 THA PYRAMID 2NITE",
  "got it",
  "how do you come up with this stuff",
  "BOOM thought leader"
]

rejected = [
  "wow learn 2 twitter",
  "nice rant.. maybe shorten it up a little",
  "UGH 140 CHARS OR LESS PLZ"
]

@hook.api_key('virtualwhatever')
@hook.command('vw')
@hook.command
def virtualwhatever(inp, api_key=None):
    '.virtualwhatever [del] <tweet> -- become a thought leader'

    if not isinstance(api_key, dict) or any(key not in api_key for key in
                                            ('consumer', 'consumer_secret', 'access', 'access_secret')):
        return "error: api keys not set"

    access = api_key.get('access')
    access_secret = api_key.get('access_secret')
    consumer = api_key.get('consumer')
    consumer_secret = api_key.get('consumer_secret')

    twitter = Twitter(auth=OAuth(access, access_secret, consumer, consumer_secret))

    if inp[:4].strip() == "del":
        tweet = twitter.statuses.user_timeline(screen_name='virtualwhatever')[0]
        text = tweet.get('text')
        twitter.statuses.destroy(id=tweet.get('id')) 
        return 'deleted last tweet: - %s' % text

    if len(inp) > 140:
         return random.choice(rejected)

    twitter.statuses.update(status=inp)
    tweet = twitter.statuses.user_timeline(screen_name='virtualwhatever')[0]
    return "%s - https://twitter.com/virtualwhatever/status/%s" % (random.choice(accepted), tweet.get('id'))
