import math

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove

TOKEN = '1736386615:AAF05MwBL5U82e_0n0h9lv1jSfhFnk9qI4Q'

a = 0
b = 0
c = 0
action = 0
equation = 0

def main():
    global dp, equation
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("equations", equations))
    dp.add_handler(CommandHandler("reference", reference))
    dp.add_handler(CommandHandler("biquadrate", biquadrate))

    updater.start_polling()
    updater.idle()


def reference(update, context):
    update.message.reply_text("Добро пожаловать в справку для этого бота")
    update.message.reply_text("/start - запуск(перезапуск) бота")
    update.message.reply_text("/equation - решение квадратных уравнений")
    update.message.reply_text("/biquadrate - решение биквадратных уравнений")
    update.message.reply_text("P.S. Бот не умеет обрабатывать корни и дроби(только десятичные)")


def start(update, context):
    reply_keyboard = [['/reference', '/equations', '/biquadrate']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    update.message.reply_text('Как этот бот может вам помочь?', reply_markup=markup)


def equations(update, context):
    global action, equation
    equation = 1
    update.message.reply_text("Введите коэффициенты для уравнения", reply_markup=ReplyKeyboardRemove())
    update.message.reply_text("ax^2 + bx + c = 0:")
    update.message.reply_text("a = ")
    dp.add_handler(MessageHandler(Filters.text, decision))


def check_a(update):
    global a, b, c, action, equation
    num = '1234567890-.'
    flag_2 = True
    a = update.message.text
    a = str(a)

    if ('.' in a and len(a) < 3) or ('.' in a and '-' in a and len(a) < 4):
        update.message.reply_text("Вы некорректно ввели первый коэффициент")
        update.message.reply_text("a = ")
        flag_2 = False
    elif '-' in a and a[0] != '-':
        update.message.reply_text("Вы некорректно ввели первый коэффициент")
        update.message.reply_text("a = ")
        flag_2 = False
    elif '.' in a:
        n = '1234567890'
        index = a.find('.')
        print(index)
        if a[index - 1] not in n or a[index + 1] not in n:
            update.message.reply_text("Вы некорректно ввели первый коэффициент")
            update.message.reply_text("a = ")
            flag_2 = False

    for i in a:
        if i not in num and action == 0 and flag_2:
            update.message.reply_text("Вы некорректно ввели первый коэффициент")
            update.message.reply_text("a = ")
            flag_2 = False
    if flag_2:
        action += 1

    if equation == 1:
        decision()
    elif equation == 2:
        decision_2()


def check_b(update):
    global a, b, c, action, equation
    num = '1234567890-.'
    flag_2 = True
    b = update.message.text
    b = str(b)

    if ('.' in b and len(b) < 3) or ('.' in b and '-' in b and len(b) < 4):
        update.message.reply_text("Вы некорректно ввели второй коэффициент")
        update.message.reply_text("b = ")
        flag_2 = False
    elif '-' in b and b[0] != '-':
        update.message.reply_text("Вы некорректно ввели второй коэффициент")
        update.message.reply_text("b = ")
        flag_2 = False
    elif '.' in b:
        n = '1234567890'
        index = b.find('.')
        print(index)
        if b[index - 1] not in n or b[index + 1] not in n:
            update.message.reply_text("Вы некорректно ввели второй коэффициент")
            update.message.reply_text("b = ")
            flag_2 = False

    for i in b:
        if i not in num and action == 1 and flag_2:
            update.message.reply_text("Вы некорректно ввели второй коэффициент")
            update.message.reply_text("b = ")
            flag_2 = False
    if flag_2:
        action += 1

    if equation == 1:
        decision()
    elif equation == 2:
        decision_2()


def check_c(update):
    global a, b, c, action, equation
    num = '1234567890-.'
    flag_2 = True
    c = update.message.text
    c = str(c)

    if ('.' in c and len(c) < 3) or ('.' in c and '-' in c and len(c) < 4):
        update.message.reply_text("Вы некорректно ввели третий коэффициент")
        update.message.reply_text("c = ")
        flag_2 = False
    elif '-' in c and c[0] != '-':
        update.message.reply_text("Вы некорректно ввели третий коэффициент")
        update.message.reply_text("c = ")
        flag_2 = False
    elif '.' in c:
        n = '1234567890'
        index = c.find('.')
        print(index)
        if c[index - 1] not in n or c[index + 1] not in n:
            update.message.reply_text("Вы некорректно ввели третий коэффициент")
            update.message.reply_text("c = ")
            flag_2 = False

    for i in c:
        if i not in num and action == 2 and flag_2:
            update.message.reply_text("Вы некорректно ввели третий коэффициент")
            update.message.reply_text("c = ")
            flag_2 = False
    if flag_2:
        action += 1

    if equation == 1:
        decision()
    elif equation == 2:
        decision_2()


def restart():
    if equation == 1:
        dp.add_handler(MessageHandler(Filters.text, decision))
    elif equation == 2:
        dp.add_handler(MessageHandler(Filters.text, decision_2))


def decision(update, context):
    global a, b, c, action, dp
    num = '1234567890-.'
    flag_2 = True
    if action == 0:
        a = update.message.text
        a_new = update.message.text
        a = str(a)

        if ('.' in a and len(a) < 3) or ('.' in a and '-' in a and len(a) < 4):
            update.message.reply_text("Вы некорректно ввели первый коэффициент")
            update.message.reply_text("a = ")
            flag_2 = False
        elif '-' in a and a[0] != '-':
            update.message.reply_text("Вы некорректно ввели первый коэффициент")
            update.message.reply_text("a = ")
            flag_2 = False
        elif '.' in a:
            n = '1234567890'
            index = a.find('.')
            print(index)
            if a[index - 1] not in n or a[index + 1] not in n:
                update.message.reply_text("Вы некорректно ввели первый коэффициент")
                update.message.reply_text("a = ")
                flag_2 = False

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

        if ('.' in b and len(b) < 3) or ('.' in b and '-' in b and len(b) < 4):
            update.message.reply_text("Вы некорректно ввели второй коэффициент")
            update.message.reply_text("b = ")
            flag_2 = False
        elif '-' in b and b[0] != '-':
            update.message.reply_text("Вы некорректно ввели второй коэффициент")
            update.message.reply_text("b = ")
            flag_2 = False
        elif '.' in b:
            n = '1234567890'
            index = b.find('.')
            print(index)
            if b[index - 1] not in n or b[index + 1] not in n:
                update.message.reply_text("Вы некорректно ввели второй коэффициент")
                update.message.reply_text("b = ")
                flag_2 = False

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

        if ('.' in c and len(c) < 3) or ('.' in c and '-' in c and len(c) < 4):
            update.message.reply_text("Вы некорректно ввели третий коэффициент")
            update.message.reply_text("c = ")
            flag_2 = False
        elif '-' in c and c[0] != '-':
            update.message.reply_text("Вы некорректно ввели третий коэффициент")
            update.message.reply_text("c = ")
            flag_2 = False
        elif '.' in c:
            n = '1234567890'
            index = c.find('.')
            print(index)
            if c[index - 1] not in n or c[index + 1] not in n:
                update.message.reply_text("Вы некорректно ввели третий коэффициент")
                update.message.reply_text("c = ")
                flag_2 = False

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
        update.message.reply_text('Коней работы', reply_markup=markup)


def biquadrate(update, context):
    global action, equation
    equation = 2
    update.message.reply_text("Введите коэффициенты для уравнения", reply_markup=ReplyKeyboardRemove())
    update.message.reply_text("ax^4 + bx^2 + c = 0:")
    update.message.reply_text("a = ")
    dp.add_handler(MessageHandler(Filters.text, decision_2))


def decision_2(update, context):
    global a, b, c, action, dp
    num = '1234567890-.'
    flag_2 = True
    if action == 0:
        a = update.message.text
        a_new = update.message.text
        a = str(a)

        if ('.' in a and len(a) < 3) or ('.' in a and '-' in a and len(a) < 4):
            update.message.reply_text("Вы некорректно ввели первый коэффициент")
            update.message.reply_text("a = ")
            flag_2 = False

        elif '-' in a and a[0] != '-':
            update.message.reply_text("Вы некорректно ввели первый коэффициент")
            update.message.reply_text("a = ")
            flag_2 = False

        elif '.' in a:
            n = '1234567890'
            index = a.find('.')
            print(index)
            if a[index - 1] not in n or a[index + 1] not in n:
                update.message.reply_text("Вы некорректно ввели первый коэффициент")
                update.message.reply_text("a = ")
                flag_2 = False

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

        if ('.' in b and len(b) < 3) or ('.' in b and '-' in b and len(b) < 4):
            update.message.reply_text("Вы некорректно ввели второй коэффициент")
            update.message.reply_text("b = ")
            flag_2 = False

        elif '-' in b and b[0] != '-':
            update.message.reply_text("Вы некорректно ввели второй коэффициент")
            update.message.reply_text("b = ")
            flag_2 = False

        elif '.' in b:
            n = '1234567890'
            index = b.find('.')
            print(index)
            if b[index - 1] not in n or b[index + 1] not in n:
                update.message.reply_text("Вы некорректно ввели второй коэффициент")
                update.message.reply_text("b = ")
                flag_2 = False

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

        if ('.' in c and len(c) < 3) or ('.' in c and '-' in c and len(c) < 4):
            update.message.reply_text("Вы некорректно ввели третий коэффициент")
            update.message.reply_text("c = ")
            flag_2 = False
        elif '-' in c and c[0] != '-':
            update.message.reply_text("Вы некорректно ввели третий коэффициент")
            update.message.reply_text("c = ")
            flag_2 = False
        elif '.' in c:
            n = '1234567890'
            index = c.find('.')
            print(index)
            if c[index - 1] not in n or c[index + 1] not in n:
                update.message.reply_text("Вы некорректно ввели третий коэффициент")
                update.message.reply_text("c = ")
                flag_2 = False

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
            x_1 = (-b + math.sqrt(discr)) / (2 * a)
            x_2 = (-b - math.sqrt(discr)) / (2 * a)
            x1 = -(math.sqrt(x_1))
            x2 = math.sqrt(x_1)
            x3 = -(math.sqrt(x_2))
            x4 = math.sqrt(x_2)
            update.message.reply_text("x1 = %.2f \nx2 = %.2f \nx3 = %.2f \nx4 = %.2f" % (x1, x2, x3, x4))
        elif discr == 0:
            x = -b / (2 * a)
            x1 = -(math.sqrt(x))
            x2 = math.sqrt(x)
            update.message.reply_text("x1 = %.2f \nx2 = %.2f" % (x1, x2))
        else:
            update.message.reply_text("Корней нет")
        action = 0

        reply_keyboard = [['/start']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
        update.message.reply_text('Коней работы', reply_markup=markup)


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
