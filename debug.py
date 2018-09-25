import os

def dprint(message):
    if 'debug' == "True" in os.environ:
        print('[DEBUG] {0}'.format(message))
    else:
        return