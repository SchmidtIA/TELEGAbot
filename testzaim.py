from telegram import Update
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import MessageHandler

button_zaim = 'Микрозайм'
button_dcard = 'Дебетовая карта'
button_ccard = 'Кредитная карта'

def button_zaim_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Это займы💸',
        reply_markup=ReplyKeyboardRemove(),
    )

def button_dcard_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Это дебетовые карты💳',
        reply_markup=ReplyKeyboardRemove(),
    )
def button_ccard_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Это кредитные карты💰',
        reply_markup=ReplyKeyboardRemove(),
    )

        
def message_handler(update: Update, context: CallbackContext):
    text = update.message.text
    if text == button_zaim:
        return button_zaim_handler(update=update, context=context)
    elif text == button_dcard:
        return button_dcard_handler(update=update, context=context)
    elif text == button_ccard:
        return button_ccard_handler(update=update, context=context)        

    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_zaim),
                KeyboardButton(text=button_dcard),
                KeyboardButton(text=button_ccard),
            ],
        ],
        resize_keyboard=True,
    )

    update.message.reply_text(
         text='Привет, я ZaimRu!\nВыбери то, что нужно, и я помогу',
         reply_markup=reply_markup,
    )


def main():
    print('Start')
    updater = Updater(
        token='1058091115:AAE_kqsq0_w4UJdtgYO9rrUyZg_bhMqcrHE',
        use_context=True,
    )
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
        main()

