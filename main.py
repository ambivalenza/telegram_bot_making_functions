import math

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove

TOKEN = '1678923601:AAHs2GdKvsjcixPC9S4C1e9y2C78Z23-V80'

a = 0
b = 0
c = 0
action = 0


def main():
    global dp
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("equation", equation))
    dp.add_handler(CommandHandler("reference", reference))
    dp.add_handler(MessageHandler(Filters.text, decision))

    updater.start_polling()
    updater.idle()


def reference(update, context):
    update.message.reply_text("Добро пожаловать в справку для этого бота")
    update.message.reply_text("/start - запуск(перезапуск) бота")
    update.message.reply_text("/equation - решение квадратных уравнений")
    update.message.reply_text("P.S. Бот не умеет обрабатывать корни и дроби(только десятичные)")


def start(update, context):
    reply_keyboard = [['/reference', '/equation']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    update.message.reply_text('Как этот бот может вам помочь?', reply_markup=markup)


def equation(update, context):
    global action
    update.message.reply_text("Введите коэффициенты для уравнения", reply_markup=ReplyKeyboardRemove())
    update.message.reply_text("ax^2 + bx + c = 0:")
    update.message.reply_text("a = ")


def check_a(update):
    global a, b, c, action
    num = '1234567890-.,'
    flag_2 = True
    a = update.message.text
    a = str(a)
    for i in a:
        if i not in num and action == 0 and flag_2:
            update.message.reply_text("Вы некорректно ввели первый коэффициент")
            update.message.reply_text("a = ")
            flag_2 = False
    if flag_2:
        action += 1
    decision()


def check_b(update):
    global a, b, c, action
    num = '1234567890-.,'
    flag_2 = True
    b = update.message.text
    b = str(b)
    for i in b:
        if i not in num and action == 1 and flag_2:
            update.message.reply_text("Вы некорректно ввели второй коэффициент")
            update.message.reply_text("b = ")
            flag_2 = False
    if flag_2:
        action += 1
    decision()


def check_c(update):
    global a, b, c, action
    num = '1234567890-.,'
    flag_2 = True
    c = update.message.text
    c = str(c)
    for i in c:
        if i not in num and action == 2 and flag_2:
            update.message.reply_text("Вы некорректно ввели третий коэффициент")
            update.message.reply_text("c = ")
            flag_2 = False
    if flag_2:
        action += 1
    decision()


def restart():
    dp.add_handler(MessageHandler(Filters.text, decision))


def decision(update, context):
    global a, b, c, action, dp
    num = '1234567890-.,'
    flag_2 = True
    if action == 0:
        a = update.message.text
        a_new = update.message.text
        a = str(a)
        for i in a:
            if i not in num and action == 0 and flag_2:
                update.message.reply_text("Вы некорректно ввели первый коэффициент")
                update.message.reply_text("a = ")
                flag_2 = False
        a_new = update.message.text
        if a == a_new and not flag_2:
            dp.add_handler(MessageHandler(Filters.text, check_a))
        elif action == 0:
            action += 1
            update.message.reply_text("b = ")
            restart()

    elif action == 1:

        b = update.message.text
        b_new = update.message.text
        b = str(b)
        for i in b:
            if i not in num and action == 1 and flag_2:
                update.message.reply_text("Вы некорректно ввели второй коэффициент")
                update.message.reply_text("b = ")
                flag_2 = False
        b_new = update.message.text
        if b == b_new and not flag_2:
            dp.add_handler(MessageHandler(Filters.text, check_b))
        elif action == 1:
            action += 1
            update.message.reply_text("c = ")
            restart()

    elif action == 2:
        c = update.message.text
        c_new = update.message.text
        c = str(c)
        for i in c:
            if i not in num and action == 2 and flag_2:
                update.message.reply_text("Вы некорректно ввели третий коэффициент")
                update.message.reply_text("c = ")
                flag_2 = False
        c_new = update.message.text
        if c == c_new and not flag_2:
            dp.add_handler(MessageHandler(Filters.text, check_c))
        elif action == 2:
            action += 1

    if action == 3:
        a = float(a)
        b = float(b)
        c = float(c)
        discr = b ** 2 - 4 * a * c
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

        reply_keyboard = [['/start']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
        update.message.reply_text('Конец работы.', reply_markup=markup)


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
