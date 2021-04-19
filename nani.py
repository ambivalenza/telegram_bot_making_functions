# Импортируем необходимые классы.
import datetime
import math

from telegram.ext import CommandHandler
from telegram.ext import Updater, MessageHandler, Filters

now = datetime.datetime.now()
TOKEN = '1678923601:AAHs2GdKvsjcixPC9S4C1e9y2C78Z23-V80'


# Определяем функцию-обработчик сообщений.
# У неё два параметра, сам бот и класс updater, принявший сообщение.
def echo(update, context):
    # У объекта класса Updater есть поле message,
    # являющееся объектом сообщения.
    # У message есть поле text, содержащее текст полученного сообщения,
    # а также метод reply_text(str),
    # отсылающий ответ пользователю, от которого получено сообщение.
    update.message.reply_text('Я получил сообщение ' + update.message.text)


def main():
    # Создаём объект updater.
    # Вместо слова "TOKEN" надо разместить полученный от @BotFather токен
    updater = Updater(TOKEN, use_context=True)

    # Получаем из него диспетчер сообщений.
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("equations", equations))
    dp.add_handler(CommandHandler("date", date))

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


# Напишем соответствующие функции.
# Их сигнатура и поведение аналогичны обработчикам текстовых сообщений.
def time(update, context):
    update.message.reply_text(now.strftime('%H:%M:%S'))


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
        print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
    elif discr == 0:
        x = -b / (2 * a)
        update.message.reply_text("x = %.2f" % x)
    else:
        update.message.reply_text("Корней нет")


def date(update, context):
    update.message.reply_text(now.strftime('%Y-%m-%d'))


# Зарегистрируем их в диспетчере рядом
# с регистрацией обработчиков текстовых сообщений.
# Первым параметром конструктора CommandHandler я
# вляется название команды.


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
