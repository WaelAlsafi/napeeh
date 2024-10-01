
from telegram.ext import CommandHandler,MessageHandler, filters, Application
from handlers.start_handler import start_command
from handlers.messages_handler import handle_response
from handlers.error_handler import error_handler, setup_logger
from handlers import *
from config_template import TOKEN
import logging
import asyncio
import nest_asyncio

nest_asyncio.apply()



setup_logger()

async def main():
    app = Application.builder().token(TOKEN).build()


    #command
    app.add_handler(CommandHandler('start', start_command))

    #messages
    app.add_handler(MessageHandler(filters.TEXT, handle_response))

    #app.add_handler(CallbackQueryHandler(button))

    # Error
    app.add_error_handler(error_handler)


    # Polls the bot
    print("Polling...")
    await app.run_polling(poll_interval=3)

if __name__ == "__main__":
        import asyncio
        asyncio.run(main())