 
from typing import Final
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputFile
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler
import three_steps

TOKEN: Final = '6626051720:AAEkF94oDKNyfiCWxDHXzZtJkTbXvxJ1FsE'
BOT_USERNAME: Final ='@doperner_bot'

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', three_steps.start_command),
                    #   CommandHandler('help', help_command),
                    #   CommandHandler('custom', custom_command),
                    #   CommandHandler('sendbuttons', send_buttons)
                    ],
        states={
            three_steps.FIRST_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, three_steps.set_first_name)],
            three_steps.LAST_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, three_steps.set_last_name)],
            three_steps.AGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, three_steps.set_age)],
        },
        fallbacks=[],
    )

    app.add_handler(conv_handler)

    # Start polling
    print('Polling...')
    app.run_polling(poll_interval=3)

