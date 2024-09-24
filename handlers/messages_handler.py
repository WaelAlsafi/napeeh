from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ContextTypes
import utils
import logging
from constants import *
from config import logging_group_id
from data_processing import df_lst, lst_of_student_id, cell_data, attendence_files
from certificate_gen import generate_certificate
from database import update_status
import os
import importlib
import time
import tele



def buttons():
    keyboard = [
        ["تهيئة الأطفال لدخول الصف الأول الابتدائي في المدرسة"],
        ["تقنيات إبداعية في دعم تميز الأبناء"],
        # ["خطوات لرفع المعنويات مع بداية عام دراسي مميز"],
        ["فنون إكساب المهارات"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    return reply_markup


    

async def handle_response(update: Update, context):
    
    if update.message:
        user_response = update.message.text
        user_info = utils.get_user_info(update)
        user_id = user_info["user_id"]
        username = user_info["username"]
        first_name = user_info["first_name"]
        name = user_info["name"]

        logging.info(f'user {name} (@{username}) says: {user_response}')
        await context.bot.send_message(chat_id=logging_group_id, text=f'user {name} (@{username}) says: {user_response}')

    user_response = user_response.strip().lower()

    if "السلام عليكم" in user_response:
        await update.message.reply_text(start_message.format(user_id=user_id, first_name=first_name), reply_markup=buttons(), parse_mode="HTML")
        return
    workshop = utils.get_workshop_number_by_name(user_response,workshops_info)
    if workshop: 
        await update.message.reply_text(choose_message, parse_mode="HTML", reply_markup=ReplyKeyboardRemove())
        user_data[user_id] = {"workshop": workshop}
        return

    try:
        workshop = user_data[user_id]["workshop"]
    except:
        await update.message.reply_text(start_message.format(user_id=user_id, first_name=first_name), reply_markup=buttons(), parse_mode="HTML")
        return
    
    if workshop in workshops_info:
        df = df_lst[workshop]
        student_id_list = lst_of_student_id(df)
        if user_response in student_id_list:
            name = cell_data(name_column, user_response, student_id_column, df)
            sex = cell_data(sex_column, user_response, student_id_column, df)
            output_path = f'{folder_path}{name}.jpg'
            if sex == 'ذكر':
                generate_certificate(name, workshop, folder_path)

            if sex == 'أنثى':
                generate_certificate(name, workshop, folder_path, female=True)

            await context.bot.send_photo(chat_id=user_id, photo=open(output_path, 'rb'))
            await context.bot.send_message(chat_id=user_id, text=restart_message.format(user_id=user_id, first_name=first_name))
            #update_status(user_id)
            await context.bot.send_message(chat_id=logging_group_id, text=f'user {name} {user_id} say {user_response} ==== match ✅')

            #delete certificate after sent
            os.remove(output_path)
            #pop user data
            user_data.pop(user_id)

        else:
            await update.message.reply_text(invalid_student_id_message)
            await context.bot.send_message(chat_id=logging_group_id, text=f'user {name} {user_id} say {user_response} ==== no match ❌')


