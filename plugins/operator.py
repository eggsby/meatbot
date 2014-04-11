from util import hook

@hook.singlethread
@hook.event('JOIN', ignorebots=False)
def op(_, conn=None, chan=None, nick=None):
    conn.cmd('MODE', [chan, '+o', nick])
