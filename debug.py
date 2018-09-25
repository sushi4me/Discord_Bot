import os

def dprint(message):
    if 'DEBUG' == True in os.environ:
        print('[DEBUG] {0}'.format(message))
    else:
        return