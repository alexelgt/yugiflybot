# Yu-Gi-Fly Bot Telegram Bot
# Copyright (C) 2021 Alexelgt

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import configparser

#=== Paths ===#
bot_folder = os.path.dirname(__file__) + "/"

#==== Config info ====#
config_info = configparser.RawConfigParser()
config_info.read(bot_folder + "config.ini")
#== Config info ==#

#=== Bot token ===#
bot_token = config_info["bot"]["token"]
