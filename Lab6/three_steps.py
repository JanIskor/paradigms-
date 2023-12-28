import asyncio

from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, ConversationHandler, MessageHandler, filters, ContextTypes

FIRST_NAME, LAST_NAME, AGE = range(3)

# Dictionary to store user information
user_info = {}

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if user_id not in user_info:
        user_info[user_id] = {}

    await update.message.reply_text('Привет! Введи свое имя')


    return FIRST_NAME

async def set_first_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    user_info[user_id]['first_name'] = update.message.text

    await update.message.reply_text("Теперь введи свою фамилию")

    return LAST_NAME

async def set_last_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    user_info[user_id]['last_name'] = update.message.text

    await update.message.reply_text(f"Отлично, {user_info[user_id]['first_name']} {user_info[user_id]['last_name']}! "
                                    "Теперь введи свой возраст")

    # Set the state to AGE
    return AGE

async def set_age(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    try:
        user_info[user_id]['age'] = int(update.message.text)
        await update.message.reply_text('Вот информация о тебе:\n'
                                        f"Имя: {user_info[user_id]['first_name']}\n"
                                        f"Фамилия: {user_info[user_id]['last_name']}\n"
                                        f"Возраст: {user_info[user_id]['age']}")
    except ValueError:
        await update.message.reply_text('Вы неправильно ввели возраст. Начните заново, написав /start.')

    # End the conversation
    return ConversationHandler.END
