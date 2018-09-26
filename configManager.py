"""
configManager.py:
    Manages config vars.
"""

# Import statements
import os

from configparser import ConfigParser


# List of necessary config vars
config_sect_list = ['DEFAULT']
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
            # Place all found config vars under the DEFAULT section
            self.config_dict['DEFAULT'] = {}
            for config_var in config_vars_list:
                try:
                    self.config_dict['DEFAULT'][config_var] = os.environ[config_var]
                except KeyError:
                    self.config_dict['DEFAULT'][config_var] = "None"
                    print("Could not find {0} as a key".format(config_var))

        print("Parsed config dictionary: {0}".format(self.config_dict))