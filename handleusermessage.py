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

from telegram.ext import CallbackContext
from telegram import Update

from time import sleep

import yugiflybot.supportmethods as support

from yugiflybot.regex import cards_info

combo_ids = {
    "2-3": "CgACAgQAAx0CR9kKNwACqthgq3YLNSvV7OJUd8lr12juMfimaQACMwIAAr4GpFKVUzYwrKpIhh8E",
    "4": "CgACAgQAAx0CR9kKNwACqvdgq4Xx6S6OBsWLSbphnB_Oo0QrYAACRgIAAvLplVJvgGqtC__wcR8E",
    "5-": "CgACAgQAAx0CR9kKNwACqypgq5ARtetfmZaE420gVc1G-agpEQACxQoAAnd-YFHaxO04cWwkrB8E"
}

def update_info(update: Update, context: CallbackContext):
    print(update)

#==== Search if a text is in any of the Regular Expressions ====#
def check_text(update: Update, context: CallbackContext):
    chat_id, chat_type, user_id, username, first_name, text, message = support.extract_update_info(update)

    combo_points = 0

    try:
        for card in cards_info:

            if bool(cards_info[card]["regex"].search(text)):
                if combo_points <= 15:
                    support.send_sticker_message(update, context, cards_info[card]["sticker_id"], replyToMessage=True)
                    sleep(1)

                combo_points += 1

        if combo_points in range(2,4):
            output_text = "💥 <b>¡Combo x{}!</b>\n\nNo está mal, fly, pero puedes hacerlo mejor.".format(combo_points)
            support.send_animation_message(update, context, combo_ids["2-3"], output_text, None, replyToMessage=True)
        elif combo_points == 4:
            output_text = "💥 <b>¡Combo x{}!</b>\n\nTu nivel de fly es increíble.".format(combo_points)
            support.send_animation_message(update, context, combo_ids["4"], output_text, None, replyToMessage=True)
        elif combo_points >= 5:
            output_text = "💥 <b>¡Combo x{}!</b>\n\n¡No puede ser! Has encontrado la última carta y liberado a Flyxodia.".format(combo_points)
            support.send_animation_message(update, context, combo_ids["5-"], output_text, None, replyToMessage=True)

    except:
        pass
#== Search if a text is in any of the Regular Expressions ==#
