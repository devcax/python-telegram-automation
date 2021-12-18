from telegram import *
from telegram.ext import *


def start_command(update,context):
    update.message.reply_text('hello')

##################################################################################


def main():

    updater = Updater('5020581541:AAHPn9-TpBIbvgtU2eZkvXFe4JNgkIGXeCA', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))


    updater.start_polling()
    updater.idle()

main()
