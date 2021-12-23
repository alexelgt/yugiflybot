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

import telegram

def extract_update_info(update):
    try:
        message = update.message
    except:
        message = None
    if message is None:
        try:
            message = update.edited_message
        except:
            message = None
    if message is None:
        try:
            message = update.channel_post
        except:
            message = None
    if message is None:
        try:
            message = update.edited_channel_post
        except:
            message = None
    if message is None:
        try:
            message = update.callback_query.message
        except:
            message = None

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

def delete_message(chat_id, message_id, context):
    try:
        context.bot.deleteMessage(chat_id=chat_id, message_id=message_id)
        return True

    except:
        return False

def delayed_delete_message_callback(context):
    chat_id, message_id = context.job.context

    delete_message(chat_id, message_id, context)

def delayed_delete_message(time: int, chat_id: int, message_id: int, context):
    try:
        if time is not None:
            context.job_queue.run_once(callback=delayed_delete_message_callback, when=time, context=[chat_id, message_id])
    except:
        pass

def send_text_message(update, context, output_text, output_buttons, deleteMessage=False, replyToMessage=False, delete_reply_after=None):
    try:
        chat_id, text, message = extract_update_info(update)

        if output_text != None:
            if replyToMessage:
                reply_to_message_id = message.message_id
            else:
                reply_to_message_id = None

            message_sent = context.bot.sendMessage(
                chat_id=chat_id,
                text=output_text,
                reply_markup=output_buttons,
                reply_to_message_id=reply_to_message_id,
                allow_sending_without_reply=True,
                parse_mode=telegram.ParseMode.HTML,
                disable_web_page_preview=True)

            if deleteMessage:
                delete_message(chat_id, message.message_id, context)

            if delete_reply_after is not None:
                delayed_delete_message(delete_reply_after, chat_id, message_sent.message_id, context)
            return message_sent
        return None
    except:
        pass

def send_sticker_message(update, context, sticker_id, deleteMessage=False, replyToMessage=False, delete_reply_after=None):
    try:
        chat_id, text, message = extract_update_info(update)

        if sticker_id != None:
            if replyToMessage:
                reply_to_message_id = message.message_id
            else:
                reply_to_message_id = None

            message_sent = context.bot.send_sticker(
                chat_id=chat_id,
                sticker=sticker_id,
                allow_sending_without_reply=True,
                reply_to_message_id=reply_to_message_id)

            if deleteMessage:
                delete_message(chat_id, message.message_id, context)

            if delete_reply_after is not None:
                delayed_delete_message(delete_reply_after, chat_id, message_sent.message_id, context)
            return message_sent
        return None
    except:
        return None

def send_animation_message(update, context, animation_id, output_text, output_buttons, deleteMessage=False, replyToMessage=False, delete_reply_after=None):
    try:
        chat_id, text, message = extract_update_info(update)

        if animation_id != None:
            if replyToMessage:
                reply_to_message_id = message.message_id
            else:
                reply_to_message_id = None

            message_sent = context.bot.send_animation(
                chat_id=chat_id,
                animation=animation_id,
                caption=output_text,
                reply_markup=output_buttons,
                allow_sending_without_reply=True,
                reply_to_message_id=reply_to_message_id,
                parse_mode=telegram.ParseMode.HTML)

            if deleteMessage:
                delete_message(chat_id, message.message_id, context)

            if delete_reply_after is not None:
                delayed_delete_message(delete_reply_after, chat_id, message_sent.message_id, context)
            return message_sent
        return None
    except:
        return None