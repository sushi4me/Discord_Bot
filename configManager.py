"""
configManager.py:
    Manages config vars.
"""

# Import statements
from util.print_util import dictionary_print
from util.convert_util import transform_config_to_dict

# List of necessary config vars
class ConfigManager:
    def __init__(self, config_file=None):
        print("ConfigManager is reading from: {0}".format(config_file))

        self._config_file = config_file
        self._config_dict = transform_config_to_dict(config_file)

        # Print the parsed dictionary
        dictionary_print(self.config_dict)

    @property
    def config_dict(self):
        return self._config_dict
    