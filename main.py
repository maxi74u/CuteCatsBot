from constants import *
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import commands, logging

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    """ get the bot started """
    print("starting...")
    # create an updater for our bot
    updater = Updater(TELEGRAM_TOKEN)
    
    # get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # assign handlers to dispatcher 👮‍♂️
    dispatcher.add_handler(CommandHandler("start", commands.start))
    dispatcher.add_handler(CommandHandler("help", commands.help))
    dispatcher.add_handler(CommandHandler("img", commands.img))
    dispatcher.add_handler(CommandHandler("fact", commands.fact))

    # if an invalid command is sent, meow 😼
    
    # start running 🏃‍♂️
    updater.start_polling(5)
    # continue running 🌚
    updater.idle() 
    # pray it works






##################################################################
# bot commands:
# (img) -> sends an image of a cat
# (fact) -> sends a cool cat fact
# (cats) -> get both
# (start) -> img+fact
# (help) -> sends description of commands and bot
##################################################################