import os
from bot import ServerBot

DIVIDER = "----"

def setupEnvironment():
    if 'prefix' in os.environ:
        BOT_PREFIX = os.environ['prefix']
    else:
        BOT_PREFIX = DEFAULT_PREFIX

    if 'token' in os.environ:
        TOKEN = os.environ['token']
    else:
        sys.exit("You forgot to set a <token> config vars in your environment!")

if __name__ == "__main__":
    # Setup environment
    setupEnvironment()

    bot = createBot()

    # Login, start bot
    bot.run(TOKEN)