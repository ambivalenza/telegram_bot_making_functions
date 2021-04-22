import math

from telegram.ext import CommandHandler
from telegram.ext import Updater, MessageHandler, Filters

TOKEN = '1678923601:AAHs2GdKvsjcixPC9S4C1e9y2C78Z23-V80'


# update.message.text

def main():
    # Создаём объект updater.
    # Вместо слова "TOKEN" надо разместить полученный от @BotFather токен
    updater = Updater(TOKEN, use_context=True)

    # Получаем из него диспетчер сообщений.
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("equations", equations))

    # Создаём обработчик сообщений типа Filters.text
    # из описанной выше функции echo()
    # После регистрации обработчика в диспетчере
    # эта функция будет вызываться при получении сообщения
    # с типом "текст", т. е. текстовых сообщений.
    text_handler = MessageHandler(Filters.text, echo)

    # Регистрируем обработчик в диспетчере.
    dp.add_handler(text_handler)
    # Запускаем цикл приема и обработки сообщений.
    updater.start_polling()

    # Ждём завершения приложения.
    # (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
    updater.idle()


def equations(update, context):
    update.message.reply_text("Введите коэффициенты для уравнения")
    update.message.reply_text("ax^2 + bx + c = 0:")
    update.message.reply_text("a = ")
    a = update.message.text
    update.message.reply_text("b = ")
    b = update.message.text
    update.message.reply_text("c = ")
    c = update.message.text

    discr = b ** 2 - 4 * a * c
    update.message.reply_text(print("Дискриминант D = %.2f" % discr))

    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        update.message.reply_text("x1 = %.2f \nx2 = %.2f" % (x1, x2))
    elif discr == 0:
        x = -b / (2 * a)
        update.message.reply_text("x = %.2f" % x)
    else:
        update.message.reply_text("Корней нет")


if __name__ == '__main__':
    main()
