from telegram import *

from telegram import update

from telegram.ext import *

from telegram.ext import updater

from telegram.ext import dispatcher

from telegram.ext import commandhandler

from telegram.ext import callbackcontext





bot = Bot("5664374727:AAEk6smo_SCdp-Km5nzFUtBO5CyxGpEaAlw")

#print(bot.get_me())

updater=Updater("5664374727:AAEk6smo_SCdp-Km5nzFUtBO5CyxGpEaAlw",use_context=True)



dispatcher=updater.dispatcher



def test_function(update:update,context:CallbackContext):

    bot.send_message(

        chat_id=update.effective_chat.id,

        text="This is my Js Bot "

        )

start_value=CommandHandler('start',test_function) 



dispatcher.add_handler(start_value)



def test_function(update:update,context:CallbackContext):

    bot.send_message(

        chat_id=update.effective_chat.id,

        text="This is my bot "

        )

help_value=CommandHandler('help',test_function) 



dispatcher.add_handler(help_value)



updater.start_polling()
