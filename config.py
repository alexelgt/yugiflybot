import os
import configparser

#=== Paths ===#
bot_folder = os.path.dirname(__file__) + "/"

config_info = configparser.RawConfigParser()
config_info.read(bot_folder + "config.ini")

#=== Bot token ===#
bot_token = config_info["bot"]["token"]

#=== IDs ===#
bot_id = 1894683001
