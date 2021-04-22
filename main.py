
import math

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = '1678923601:AAHs2GdKvsjcixPC9S4C1e9y2C78Z23-V80'

odds = {}

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("equations", equations))
    dp.add_handler(MessageHandler(Filters.text, decision))
    updater.start_polling()
    updater.idle()


def equations(update, context):
    activity = 0
    update.message.reply_text("Введите коэффициенты для уравнения")
    update.message.reply_text("ax^2 + bx + c = 0:")


def decision(update, context):
    update.message.reply_text("a = ")

    a = update.message.text

    update.message.reply_text("b = ")
    b = update.message.text
    update.message.reply_text("c = ")
    c = update.message.text

    discr = int(b) ** 2 - 4 * int(a) * int(c)
    update.message.reply_text("Дискриминант D = %.2f" % discr)

    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        update.message.reply_text("x1 = %.2f \nx2 = %.2f" % (x1, x2))
    elif discr == 0:
        x = -b / (2 * a)
        update.message.reply_text("x = %.2f" % x)
    else:
        update.message.reply_text("Корней нет")


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
