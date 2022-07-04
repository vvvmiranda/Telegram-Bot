from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

#Bot using telegram library.

updater = Updater("insert key from botfather", use_context=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text('welcome message')

def help (update: Update, context: CallbackContext):
    update.message.reply_text('help text showing available commands')  
    
def linkedin(update: Update, context: CallbackContext):
    update.message.reply_text('your linkedin')

def github(update: Update, context: CallbackContext):
    update.message.reply_text('your github link')

def gmail(update: Update, context: CallbackContext):
  update.message.reply_text('your email')

def youtube(update: Update, context: CallbackContext):
    update.message.reply_text('YouTube => https://youtu.be/dQw4w9WgXcQ')

def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "error message when running an unknown text '%s'" % update.message.text)

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "the command '%s' is not recognized by the bot." % update.message.text)

# The handles that associates what the user types and which function to run, respectively. Do NOT change start.

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedin))
updater.dispatcher.add_handler(CommandHandler('Email', gmail))
updater.dispatcher.add_handler(CommandHandler('github', github))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
