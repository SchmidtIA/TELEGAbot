import webbrowser
from telegram import Bot
from telegram import ParseMode
from telegram import Update
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import CallbackQueryHandler
from telegram.ext import CommandHandler


button_zaim = 'Микрозайм'
button_dcard = 'Дебетовая карта'
button_ccard = 'Кредитная карта'
# переменные callback
# ZAIM
CALLBACK_BUTTON1_TURBO = "callback_button1"
CALLBACK_BUTTON2_GLAV = "callback_button2"
CALLBACK_BUTTON3_ZAIMER = "callback_button3"
CALLBACK_BUTTON4_WEBB = "callback_button4"
CALLBACK_BUTTON5_WEBZ = "callback_button5"
CALLBACK_BUTTON6_DOZP = "callback_button6"
CALLBACK_BUTTON7_SROCH = "callback_button7"
CALLBACK_BUTTON8_BOOS = "callback_button8"
CALLBACK_BUTTON9_VIVA = "callback_button9"
CALLBACK_BUTTON10_BACK = "callback_button10"
# DEB CARD
CB2_1_HOME = "callback_button2_1"
CB2_2_TINK = "callback_button2_2"
CB2_3_OPEN = "callback_button2_3"
CB2_4_ROK = "callback_button2_4"
# CRED CARD
CB3_1_ALFA = "callback_button3_1"
CB3_2_TINK = "callback_button3_2"
CB3_3_HOM = "callback_button3_3"
CB3_4_ROS = "callback_button3_4"
CB3_5_ROS2 = "callback_button3_5"
CB3_6_OPEN = "callback_button3_6"
CB3_7_SOV = "callback_button3_7"
CB3_8_HAL = "callback_buttom3_8"
# КЛАВА ПОД СООБЩЕНИЕМ название
TITLES = {
    CALLBACK_BUTTON1_TURBO: "ТУРБОЗАЙМ ✅",
    CALLBACK_BUTTON2_GLAV: "Главзайм ✅",
    CALLBACK_BUTTON3_ZAIMER: "Займер ✅",
    CALLBACK_BUTTON4_WEBB: "Webbankir ✅",
    CALLBACK_BUTTON5_WEBZ: "ВЕБ-ЗАЙМ ✅",
    CALLBACK_BUTTON6_DOZP: "ДоЗарплаты ✅",
    CALLBACK_BUTTON7_SROCH: "Срочноденьги онлайн ✅",
    CALLBACK_BUTTON8_BOOS: "Boostra ✅",
    CALLBACK_BUTTON9_VIVA: "VIVA деньги ✅",
    # D card
    CB2_1_HOME: "Home Credit - дебетовая карта Польза ❌",
    CB2_2_TINK : "Тинькофф Банк - Tinkoff Black 🔶",
    CB2_3_OPEN: "Банк Открытие - дебетовая карта 🔵",
    CB2_4_ROK: " Рокетбанк - РокетКарта 🔺",
    # c card
    CB3_1_ALFA: 'АльфаБанк - кредитная карта "100 дней без %" 💯',
    CB3_2_TINK: "Тинькофф Банк - кредитная карта ☑",
    CB3_3_HOM: 'Home Credit - карта рассрочки "Свобода" ◼',
    CB3_4_ROS: "РОСБАНК - кредитная карта «#120подНОЛЬ» 🔴",
    CB3_5_ROS2: 'РОСБАНК - кредитная карта "Можно ВСЁ!" ⚜',
    CB3_6_OPEN: "Банк Открытие - Кредитная карта 120 дней 🌀",
    CB3_7_SOV: "Совесть - карта беспроцентной рассрочки ©",
    CB3_8_HAL: "Халва - карта рассрочки ⭕",
}


def button_zaim_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Это займы💸',
        reply_markup=get_base_inline_keyboard(),
    )


def button_dcard_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Это дебетовые карты💳',
        reply_markup=get_base_inline_keyboard_2(),
    )


def button_ccard_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Это кредитные карты💰',
        reply_markup=get_base_inline_keyboard_3(),
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


# клавиатура под сообщением
def get_base_inline_keyboard():
    keyboard = [

        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON1_TURBO], callback_data=CALLBACK_BUTTON1_TURBO),
        ],
        [    InlineKeyboardButton(TITLES[CALLBACK_BUTTON2_GLAV], callback_data=CALLBACK_BUTTON2_GLAV),

        ],
        [    InlineKeyboardButton(TITLES[CALLBACK_BUTTON3_ZAIMER], callback_data=CALLBACK_BUTTON3_ZAIMER),

        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON4_WEBB], callback_data=CALLBACK_BUTTON4_WEBB),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON5_WEBZ], callback_data=CALLBACK_BUTTON5_WEBZ),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON6_DOZP], callback_data=CALLBACK_BUTTON6_DOZP),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON7_SROCH], callback_data=CALLBACK_BUTTON7_SROCH),
        ],

        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON8_BOOS], callback_data=CALLBACK_BUTTON8_BOOS),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON9_VIVA], callback_data=CALLBACK_BUTTON9_VIVA),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

def get_base_inline_keyboard_2():
    keyboard = [
        [
          InlineKeyboardButton(TITLES[CB2_1_HOME], callback_data=CB2_1_HOME),
        ],
        [
          InlineKeyboardButton(TITLES[CB2_2_TINK], callback_data=CB2_2_TINK),
        ],
        [
          InlineKeyboardButton(TITLES[CB2_3_OPEN], callback_data=CB2_3_OPEN),
        ],
        [
          InlineKeyboardButton(TITLES[CB2_4_ROK], callback_data=CB2_4_ROK),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

def get_base_inline_keyboard_3():
    keyboard = [
        [
          InlineKeyboardButton(TITLES[CB3_1_ALFA], callback_data=CB3_1_ALFA),
        ],
        [  
          InlineKeyboardButton(TITLES[CB3_2_TINK], callback_data=CB3_2_TINK),
        ],
        [
          InlineKeyboardButton(TITLES[CB3_3_HOM], callback_data=CB3_3_HOM),
        ],
        [
          InlineKeyboardButton(TITLES[CB3_4_ROS], callback_data=CB3_4_ROS),
        ],
        [
          InlineKeyboardButton(TITLES[CB3_5_ROS2], callback_data=CB3_5_ROS2),
        ],
        [
          InlineKeyboardButton(TITLES[CB3_6_OPEN], callback_data=CB3_6_OPEN),
        ],
        [
          InlineKeyboardButton(TITLES[CB3_7_SOV], callback_data=CB3_7_SOV),
        ],
        [
          InlineKeyboardButton(TITLES[CB3_8_HAL], callback_data=CB3_8_HAL),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

# обработка событий keyboard
def keyboard_callback_handler(bot: Bot, update: Update, chat_data=None, **kwargs):
    query = update.callback_query
    data = query.data
    now = datetime.datetime.now()

if CB2_1_HOME == CB2_1_HOME:
    webbrowser.open("https://go.leadgid.ru/aff_c?offer_id=2509&aff_id=60785")

    


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
