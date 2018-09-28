import os

from configparser import ConfigParser


config_sect_list = ['DEFAULT']
config_vars_list = ['prefix', 'debug', 'discord_token', 'giphy_token']


def transform_config_to_dict(config_file):
        config_dict = {}

        # Parse through the config file
        if config_file is not None:
            config_parser = ConfigParser()
            config_parser.read(config_file)
            
            for section in config_parser.sections():
                config_dict[section] = {}

                for option in config_parser.options(section):
                    try:
                        config_dict[section][option] = config_parser.get(section, option)
                    except:
                        print("Exception for {0}: {1}".format(section, option))
        # Get the config vars from the environment
        else:
            # Place all found config vars under the DEFAULT section
            config_dict['DEFAULT'] = {}
            for config_var in config_vars_list:
                try:
                    config_dict['DEFAULT'][config_var] = os.environ[config_var]
                except KeyError:
                    config_dict['DEFAULT'][config_var] = "None"
                    print("Could not find {0} as a key".format(config_var))

        return config_dict