



async def edit_message( chat_id, message_id, text, context) -> None:
    await context.bot.edit_message_text(chat_id=chat_id,
                                        message_id=message_id,
                                        text=text)
