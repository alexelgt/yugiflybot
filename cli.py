#!/usr/bin/python3

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

from telegram.ext import Updater, MessageHandler, Filters
from telegram.utils.request import Request
from telegram.bot import Bot

import yugiflybot.handleusermessage as handleusermessage

from yugiflybot.regex import FLY_GROUPS_REGEX, CHECK_TEXT_REGEX, ANIMATION_TEXT_REGEX

from yugiflybot.config import bot_token

#==== Bot initial set up ====#
workers = 12
con_pool_size = workers + 4

request = Request(con_pool_size=con_pool_size)
bot = Bot(bot_token, request=request)
updater = Updater(bot=bot, workers=workers)

dispatcher = updater.dispatcher
#== Bot initial set up ==#

#==== Message handlers ====#
# Message sent
dispatcher.add_handler(MessageHandler(callback=handleusermessage.check_text, filters=Filters.text & (Filters.regex(CHECK_TEXT_REGEX) | Filters.regex(FLY_GROUPS_REGEX)) & Filters.update.message & Filters.chat_type.groups, run_async=True))

dispatcher.add_handler(MessageHandler(callback=handleusermessage.check_animation, filters=Filters.text & Filters.regex(ANIMATION_TEXT_REGEX) & Filters.update.message & Filters.chat_type.groups, run_async=True))

# dispatcher.add_handler(MessageHandler(callback=handleusermessage.update_info, filters=(Filters.sticker | Filters.animation), run_async=True))
#== Message handlers ==#

print("Bot started")
updater.start_polling()
updater.idle()
