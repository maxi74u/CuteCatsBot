from constants import DESCRIPTION
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from cats import *

def start(update: Update, context: CallbackContext) -> None:
    """ send an img, fact, welcome user, send description of commands """
    user = update.effective_user
    tmp_cat = Cat()
    update.message.reply_text(f'Meow {user.first_name}!')
    update.message.reply_text(f'{tmp_cat.img}')
    update.message.reply_text(f'{tmp_cat.fact}',)
    update.message.reply_text(f'{DESCRIPTION}',)

def help(update: Update, context: CallbackContext) -> None:
    """ help user by sending a list of commands"""
    update.message.reply_text(f'{LIST}')

def img(update: Update, context: CallbackContext) -> None:
    ''' send an image of a cute cat '''
    tmp_cat = Cat()
    update.message.reply_text(f'{tmp_cat.img}')

def fact(update: Update, context: CallbackContext) -> None:
    ''' send an image of a cute cat '''
    tmp_cat = Cat()
    update.message.reply_text(f'{tmp_cat.fact}')