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

from typing import Any, Optional

from telegram import Update, Message


def extract_message_from_update(
    update: Update
) -> Optional[Any]:
    # List of attributes to check in order of priority
    attrs = ['message', 'edited_message', 'channel_post', 'edited_channel_post', 'callback_query.message', 'my_chat_member']

    for attr in attrs:
        try:
            # Split the attribute string by dots and access each level iteratively
            current_obj = update
            for part in attr.split('.'):
                current_obj = getattr(current_obj, part)

            if current_obj is not None:
                return current_obj
        except AttributeError:
            pass

    # If no message was found after checking all attributes
    return None


def extract_update_info(
    update: Update
) -> tuple[Optional[int], Optional[str], Optional[Message]]:
    message = extract_message_from_update(update)

    try:
        text = message.text
    except:
        text = None
    if text is None:
        try:
            text = message.caption
        except:
            text = None

    try:
        chat_id = message.chat.id
    except:
        chat_id = None

    return chat_id, text, message
