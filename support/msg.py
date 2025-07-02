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

from telegram.ext import ContextTypes
from telegram.constants import ParseMode

from yugiflybot import config

from yugiflybot.support import extract


async def delete_message(
    chat_id: int,
    message_id: int,
    context: ContextTypes.DEFAULT_TYPE
) -> bool:
    try:
        await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
        return True
    except:
        return False


async def delayed_delete_message_callback(
    context: ContextTypes.DEFAULT_TYPE
) -> None:
    chat_id, message_id = context.job.data

    await delete_message(chat_id, message_id, context)


def delayed_delete_message(
    time: int,
    chat_id: int,
    message_id: int,
    context: ContextTypes.DEFAULT_TYPE
) -> None:
    try:
        if time is not None:
            context.job_queue.run_once(callback=delayed_delete_message_callback, when=time, data=[chat_id, message_id])
    except:
        pass


async def send_text_message(update, context, output_text, output_buttons, deleteMessage=False, replyToMessage=False, delete_reply_after=None):
    try:
        chat_id, _, message = extract.extract_update_info(update)

        if output_text is not None:
            if replyToMessage:
                reply_to_message_id = message.message_id
            else:
                reply_to_message_id = None

            message_sent = await context.bot.sendMessage(
                chat_id=chat_id,
                text=output_text,
                reply_markup=output_buttons,
                reply_to_message_id=reply_to_message_id,
                allow_sending_without_reply=True,
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=True)

            if deleteMessage:
                await delete_message(chat_id, message.message_id, context)

            if delete_reply_after is not None:
                delayed_delete_message(
                    delete_reply_after, chat_id, message_sent.message_id, context)
            return message_sent
        return None
    except:
        pass


async def send_photo_message(update, context, photo_name, output_text, output_buttons, deleteMessage=False, replyToMessage=False, delete_reply_after=None):
    try:
        chat_id, _, message = extract.extract_update_info(update)

        if output_text is not None:
            output_photo_path = config.PHOTO_PATH + photo_name

            if replyToMessage:
                reply_to_message_id = message.message_id
            else:
                reply_to_message_id = None

            message_sent = await context.bot.sendPhoto(
                chat_id=chat_id,
                photo=open(output_photo_path, "rb"),
                caption=output_text,
                reply_markup=output_buttons,
                allow_sending_without_reply=True,
                reply_to_message_id=reply_to_message_id,
                parse_mode=ParseMode.HTML)

            if deleteMessage:
                await delete_message(chat_id, message.message_id, context)

            if delete_reply_after is not None:
                delayed_delete_message(
                    delete_reply_after, chat_id, message_sent.message_id, context)
            return message_sent
        return None
    except:
        return None


async def send_sticker_message(update, context, sticker_id, deleteMessage=False, replyToMessage=False, delete_reply_after=None):
    try:
        chat_id, _, message = extract.extract_update_info(update)

        if sticker_id is not None:
            if replyToMessage:
                reply_to_message_id = message.message_id
            else:
                reply_to_message_id = None

            message_sent = await context.bot.send_sticker(
                chat_id=chat_id,
                sticker=sticker_id,
                allow_sending_without_reply=True,
                reply_to_message_id=reply_to_message_id)

            if deleteMessage:
                await delete_message(chat_id, message.message_id, context)

            if delete_reply_after is not None:
                delayed_delete_message(
                    delete_reply_after, chat_id, message_sent.message_id, context)
            return message_sent
        return None
    except:
        return None


async def send_animation_message(update, context, animation_id, output_text, output_buttons, deleteMessage=False, replyToMessage=False, delete_reply_after=None):
    try:
        chat_id, _, message = extract.extract_update_info(update)

        if animation_id is not None:
            if replyToMessage:
                reply_to_message_id = message.message_id
            else:
                reply_to_message_id = None

            message_sent = await context.bot.send_animation(
                chat_id=chat_id,
                animation=animation_id,
                caption=output_text,
                reply_markup=output_buttons,
                allow_sending_without_reply=True,
                reply_to_message_id=reply_to_message_id,
                parse_mode=ParseMode.HTML)

            if deleteMessage:
                await delete_message(chat_id, message.message_id, context)

            if delete_reply_after is not None:
                delayed_delete_message(
                    delete_reply_after, chat_id, message_sent.message_id, context)
            return message_sent
        return None
    except:
        return None
