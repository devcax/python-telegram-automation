from telegram import *
from telegram.ext import *


def start_command(update,context):
    update.message.reply_text('hello')

##################################################################################


def main():

    updater = Updater('YOUR_API', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))


    updater.start_polling()
    updater.idle()

main()
