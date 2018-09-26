"""
configManager.py:
    Manages config vars.
"""

# Import statements
from configparser import ConfigParser


# List of necessary config vars
config_vars_list = ['prefix', 'debug', 'discord_token', 'giphy_token']


class ConfigManager:
    def __init__(self, config_file=None):
        self.config_file = config_file
        self.config_dict = {}

        # Parse through the config file
        if config_file is not None:
            parser = ConfigParser()
            self.config_dict = parser.read(self.config_file)
        # Get the config vars from the environment
        else:
            for config_var in config_vars_list:
                self.config_dict[config_var] = os.environ[config_var]

        print("Parsed config dictionary: {0}".format(self.config_dict))