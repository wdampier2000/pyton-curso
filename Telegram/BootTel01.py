#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.
# test test

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.

Done! Congratulations on your new bot. You will find it at t.me/NubeProbe_bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.

Use this token to access the HTTP API:
2001629979:AAEIlHZKdiTjSFdXXPvLy1uytUJsx5Nu_A8
Keep your token secure and store it safely, it can be used by anyone to control your bot.

For a description of the Bot API, see this page: https://core.telegram.org/bots/api
"""

import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext) -> None:
    #Send a message when the command /start is issued.
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    #Send a message when the command /help is issued.#
    update.message.reply_text('Help!')

def echo(update: Update, context: CallbackContext) -> None:
    #Echo the user message.
    #update.message.reply_text(update.message.text)
    update.message.reply_text("No entiendo!")
    print(CallbackContext)

#func de contestacion
def rmi_command(update: Update, context: CallbackContext) -> None:
    #Echo the user message.
    update.message.reply_text("aca el mesaje")
    print(CallbackContext)

def main() -> None:
    #Start the bot.#
    # Create the Updater and pass it your bot's token.
    updater = Updater("2001629979:AAEIlHZKdiTjSFdXXPvLy1uytUJsx5Nu_A8")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("rmi", rmi_command))

    # on non command i.e message - echo the message on Telegram
  
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    
    main()
    #update.message.reply_text("Informacion")


