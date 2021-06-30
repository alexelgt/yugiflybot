from telegram.ext import Updater, MessageHandler, Filters
from telegram.utils.request import Request
from telegram.bot import Bot

import yugiflybot.handleusermessage as handleusermessage

from yugiflybot.regex import CHECK_TEXT_REGEX

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
dispatcher.add_handler(MessageHandler(callback=handleusermessage.check_text, filters=Filters.text & Filters.regex(CHECK_TEXT_REGEX) & Filters.update.message & (Filters.chat_type.groups | Filters.chat_type.private), run_async=True))

# dispatcher.add_handler(MessageHandler(callback=handleusermessage.update_info, filters=(Filters.sticker | Filters.animation), run_async=True))
#== Message handlers ==#

print("Bot started")
updater.start_polling()
updater.idle()
