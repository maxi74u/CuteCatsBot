import os

# the telegram bot api key
TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']

# catsapi key
CAT_API_KEY = os.environ['CAT_API_KEY']
# the url I use to send get requests for imgs
CAT_API_URL = 'https://api.thecatapi.com/v1/images/search'

# the url used to send get requests for facts
MEOW_API_URL = "https://meowfacts.herokuapp.com/"

#the Description for the bot, presented with /start
DESCRIPTION = '''
CUTECATSPICSFACTSBOT is a bot that sends you cute cat pics and facts

for a full list of commands use /help

developed by: https://github.com/maxi74u

'''

#the list of commands the bot supports, used with /help
LIST = '''
/start => start bot.
/help => get help.
/img => get cat pic.
/fact => get a cat fact.
'''