#!/usr/bin/python3

# Yu-Gi-Fly Bot Telegram Bot
# Copyright (C) 2025 Alexelgt

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

from telegram.ext import Application, MessageHandler, filters

from yugiflybot import handleusermessage, config

from yugiflybot.classes import CustomAIORateLimiter

from yugiflybot.regex import FLY_GROUPS_REGEX, CARDS_TEXT_REGEX, ANIMATION_PHOTOS_TEXT_REGEX

# === Bot initial set up === #
application = Application.builder().token(config.BOT_TOKEN).rate_limiter(
    CustomAIORateLimiter(overall_max_rate=0, max_retries=1)).build()

# ==== Message handlers ==== #
application.add_handler(MessageHandler(callback=handleusermessage.check_cards_text, filters=filters.TEXT & (filters.Regex(
    CARDS_TEXT_REGEX) | filters.Regex(FLY_GROUPS_REGEX)) & filters.UpdateType.MESSAGE & filters.ChatType.GROUPS, block=False))

application.add_handler(MessageHandler(callback=handleusermessage.check_animations_photos_text, filters=filters.TEXT & filters.Regex(
    ANIMATION_PHOTOS_TEXT_REGEX) & filters.UpdateType.MESSAGE & filters.ChatType.GROUPS, block=False))

# application.add_handler(MessageHandler(callback=handleusermessage.update_info, filters=(filters.Sticker.ALL | filters.ANIMATION), block=False))
# == Message handlers == #

print("Bot started")
application.run_polling()
