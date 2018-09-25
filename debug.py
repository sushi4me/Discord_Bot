import os

def dprint(message):
    if 'debug' in os.environ && os.environ['debug'].lower() == "true":
        print('[DEBUG] {0}'.format(message))
    else:
        return