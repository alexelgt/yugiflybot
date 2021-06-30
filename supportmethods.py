import telegram

def extract_user_info(user):
    try:
        user_id = user.id
    except:
        user_id = None

    try:
        username = user.username
    except:
        username = None

    try:
        first_name = user.first_name
    except:
        first_name = None

    try:
        last_name = user.last_name
    except:
        last_name = None

    return user_id, username, first_name, last_name

def extract_update_info(update):
    isCallback = False
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
            isCallback = True
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

    if isCallback:
        from_user = update.callback_query.from_user
    else:
        from_user = message.from_user

    user_id, username, first_name = extract_user_info(from_user)[:3]

    try:
        chat_id = message.chat.id
    except:
        chat_id = None
    try:
        chat_type = message.chat.type
    except:
        chat_type = None

    return chat_id, chat_type, user_id, username, first_name, text, message

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

def send_sticker_message(update, context, sticker_id, deleteMessage=False, replyToMessage=False, delete_reply_after=None):
    try:
        chat_id, chat_type, user_id, username, first_name, text, message = extract_update_info(update)

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
        chat_id, chat_type, user_id, username, first_name, text, message = extract_update_info(update)

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