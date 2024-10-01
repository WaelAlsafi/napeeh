from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from .messages_handler import buttons
from database import add_user_to_db
from constants_template import user_data, start_message


async def start_command(update: Update, context):
    if user_data.get(update.message.from_user.id) is not None:
        user_data[update.message.from_user.id] = {}

    user = update.message.from_user
    user_id = user.id
    username = user.username

    first_name = update.message.from_user.first_name
    last_name = user.last_name
    name = ""
    if first_name:
        name = first_name
    if last_name:
        name = name + " " + last_name

    #add_user_to_db(user_id, username, name)

    await update.message.reply_text(start_message.format(user_id=user_id, first_name=first_name), reply_markup=buttons(), parse_mode="HTML")
