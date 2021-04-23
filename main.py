import math

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = '1678923601:AAHs2GdKvsjcixPC9S4C1e9y2C78Z23-V80'

a = 0
b = 0
c = 0
action = 0


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("equations", equations))
    dp.add_handler(MessageHandler(Filters.text, decision))
    updater.start_polling()
    updater.idle()


def equations(update, context):
    global action
    update.message.reply_text("Введите коэффициенты для уравнения")
    update.message.reply_text("ax^2 + bx + c = 0:")
    update.message.reply_text("a = ")
    action += 1


def decision(update, context):
    global a, b, c, action
    if action == 1:
        a += int(update.message.text)
        update.message.reply_text("b = ")
        action += 1
    elif action == 2:
        b += int(update.message.text)
        update.message.reply_text("c = ")
        action += 1
    elif action == 3:
        c += int(update.message.text)
        discr = int(b) ** 2 - 4 * int(a) * int(c)
        update.message.reply_text(f"Дискриминант D = {discr}")
        print(a, b, c)
        if discr > 0:
            x1 = (-b + math.sqrt(discr)) / (2 * a)
            x2 = (-b - math.sqrt(discr)) / (2 * a)
            update.message.reply_text("x1 = %.2f \nx2 = %.2f" % (x1, x2))
        elif discr == 0:
            x = -b / (2 * a)
            update.message.reply_text("x = %.2f" % x)
        else:
            update.message.reply_text("Корней нет")
        action = 0


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
