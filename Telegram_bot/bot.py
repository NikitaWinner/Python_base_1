from telegram import Update
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import MessageHandler


button_help = 'Подарок!'


def button_help_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Спермак тебе в сраку!',
        reply_markup=ReplyKeyboardRemove(),
    )


def message_handler(update: Update, context: CallbackContext):
    text = update.message.text
    if text == button_help:
        return button_help_handler(update=update, context=context)

    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_help)
            ],
        ],
        resize_keyboard=True,
    )
    update.message.reply_text(
        text='Нажми на кнопку ниже, что бы получить подарок',
        reply_markup=reply_markup,
    )


def main():
    updater = Updater(
        token='5246139889:AAGs9DlzSshO40nCcR8kHYx8G4LSHwZv0Ss',
        use_context=True,
    )
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
    # Filters.text
    # Filters.all