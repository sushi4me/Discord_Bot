import const
import os
from bot import ServerBot

def setupEnvironment():
    config_vars = {}
    config_vars['prefix'] = "!"
    config_vars['token'] = "none"
    return config_vars

def getEnvironmentConfigVars(temp_dict):
    for key, value in temp_dict.items():
        if key in os.environ:
            temp_dict[key] = os.environ[key]
    return temp_dict

if __name__ == "__main__":
    # Setup environment
    temp_dict = setupEnvironment()
    config_dict = getEnvironmentConfigVars(temp_dict)

    # Create ServerBot object
    description = "A small bot."
    bot = ServerBot(config_dict, description)