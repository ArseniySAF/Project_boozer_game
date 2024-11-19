import telebot #импортирую библиотеку для создания чат-бота
from telebot import types #импортирую модуль для создания кнопок
import random #импорттирую библиотеку для рандомного выбора чисел и предметов

#токен бота
bot = telebot.TeleBot('7433564468:AAF2Ha7iH2k_fb4I-0fOGEhTmOj0rwYWvcw')


#Начало работы по кнопке start
@bot.message_handler(commands=['start'])
def Start(message):
    """ Функция отслеживает комманду /start """

    markup =  types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Поехали')
    markup.row(btn1)
    mess = f"Привет, {message.from_user.first_name}! Цель этой игры дойти до дома после дня рождения друга, где ты отдыхал и веселился."
    bot.send_message(message.chat.id, mess, reply_markup=markup)


@bot.message_handler()
def Game(message):
    """ Функция отслеживает комманды, вводимые пользователем """

    if message.text == "Поехали":
        mess_first_pos = '''Твоя начальная позиция
                                😀 * * * * 🏠 

                                        '''
        bot.send_message(message.chat.id, mess_first_pos)
        move_chance = random.randint(1, 2) >= 2
        if move_chance == False:
            markup = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("Поехали")
            markup.add(btn1)
            mess_loose =  ''' Упс, неповезло. Давай по новой
                        😀 * * * * 🏠
                    '''
            bot.send_message(message.chat.id, mess_loose, reply_markup=markup)
        if move_chance:
            markup = types.ReplyKeyboardMarkup()
            btn1_win = types.KeyboardButton('Идем дальше')
            markup.add(btn1_win)
            mess_win = ''' Ты на шаг ближе к успеху!
                      🟢 😀 * * * 🏠      
            '''
            bot.send_message(message.chat.id, mess_win, reply_markup=markup)
    if message.text == "Идем дальше":
        mess_greet = "Ура, ты на второй улице!"
        bot.send_message(message.chat.id, mess_greet)
        mess_about_item = '''Ты видишь неопознанный предмет
                        Поднять его?
                        Да/Нет
                        '''
        markup = types.ReplyKeyboardMarkup()
        btn_pickup_yes = types.KeyboardButton('Да, поднять 1 предмет')
        btn_pickuo_no = types.KeyboardButton('Нет, не буду поднимать 1 предмет')
        markup.row(btn_pickup_yes, btn_pickuo_no)
        bot.send_message(message.chat.id, mess_about_item, reply_markup=markup)
    if message.text == "Да, поднять 1 предмет":
        items_list = ["Номер Друга", "Боржоми", "Бутылка Пива", "Бутылка водки"]
        item = random.choice(items_list)
        if item == "Номер Друга":
            bot.send_message(message.chat.id, "Ты нашел номер друга! Он поможет провести тебя через улицу. Твои шансы 60%")
            move_chance_friend = random.randint(1, 10) >= 6
            if move_chance_friend == False:
                markup = types.ReplyKeyboardMarkup()
                btn1 = types.KeyboardButton("Поехали")
                markup.row(btn1)
                mess = ''' 
                        Упс, неповезло. Давай по новой
                        😀 * * * * 🏠
                    '''
                bot.send_message(message.chat.id, mess, reply_markup=markup)
            if move_chance_friend:
                markup = types.ReplyKeyboardMarkup()
                btn_next2 = types.KeyboardButton("Идем на 3 улицу! Ура!")
                markup.row(btn_next2)
                mess_win_with_friend_street1 = ''' 
                        Ура, ты прошел улицу!!!
                     🟢 🟢 😀 * 🏠
                    '''
                bot.send_message(message.chat.id, mess_win_with_friend_street1, reply_markup=markup)
        elif item == "Боржоми":
            bot.send_message(message.chat.id, '''Вау! Ты нашел бутылку Боржоми! Твои шансы пройти улицу 100% 
                                                                    Определнно - ты везунчик!  ''')
            move_chance_borjomi = random.randint(1, 100) <= 100
            if move_chance_borjomi:
                markup = types.ReplyKeyboardMarkup()
                btn_next2 = types.KeyboardButton("Идем на 3 улицу! Ура!")
                markup.row(btn_next2)
                mess_win_with_friend_street1 = ''' 
                        Ура, ты прошел улицу!!!
                    🟢 🟢 😀 * 🏠
                    '''
                bot.send_message(message.chat.id, mess_win_with_friend_street1, reply_markup=markup)
        elif item == "Бутылка Пива":
            bot.send_message(message.chat.id, "Ты нашел бутылку пива. Ой ой праздник продолжается... Твой шанс пройти улицу равен 40%")
            move_chance_pivo = random.randint(1, 10) <= 4
            if move_chance_pivo == False:
                markup = types.ReplyKeyboardMarkup()
                btn1 = types.KeyboardButton("Поехали")
                markup.row(btn1)
                mess = ''' 
                        Упс, неповезло. Давай по новой
                        😀 * * * * 🏠
                    '''
                bot.send_message(message.chat.id, mess, reply_markup=markup)
            if move_chance_pivo:
                markup = types.ReplyKeyboardMarkup()
                btn_next2 = types.KeyboardButton("Идем на 3 улицу! Ура!")
                markup.row(btn_next2)
                mess_win_with_friend_street1 = ''' 
                        Ура, ты прошел улицу!!!
                    🟢 🟢 😀 * 🏠
                    '''
                bot.send_message(message.chat.id, mess_win_with_friend_street1, reply_markup=markup)
        elif item == "Бутылка водки":
            bot.send_message(message.chat.id, "Тебе выпала бутылка водки... Ой ой... Это было зряяя. Твой шанс пройти улицу равен 10%")
            move_chance_vodka = random.randint(1, 10) >= 10
            if move_chance_vodka == False:
                markup = types.ReplyKeyboardMarkup()
                btn1 = types.KeyboardButton("Поехали")
                markup.row(btn1)
                mess = ''' 
                        Упс, неповезло. Давай по новой
                        😀 * * * * 🏠
                    '''
                bot.send_message(message.chat.id, mess, reply_markup=markup)
            if move_chance_vodka:
                markup = types.ReplyKeyboardMarkup()
                btn_next2 = types.KeyboardButton("Идем на 3 улицу! Ура!")
                markup.row(btn_next2)
                mess_win_with_friend_street1 = ''' 
                        Ура, ты прошел улицу!!!
                    🟢 🟢 😀 * 🏠
                    '''
                bot.send_message(message.chat.id, mess_win_with_friend_street1, reply_markup=markup)
    if message.text == "Нет, не буду поднимать 1 предмет":
        move_chance_without_1_item = random.randint(1, 2) >= 2
        if move_chance_without_1_item == False:
            markup = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("Поехали")
            markup.add(btn1)
            mess_loose_without_friend_street1 =  ''' Упс, неповезло. Давай по новой
                        😀 * * * * 🏠
                    '''
            bot.send_message(message.chat.id, mess_loose_without_friend_street1, reply_markup=markup)
        if move_chance_without_1_item:
            markup = types.ReplyKeyboardMarkup()
            btn1_win = types.KeyboardButton('Идем на 3 улицу! Ура!')
            markup.add(btn1_win)
            mess_win_without_friend_street1 = ''' Ты на шаг ближе к успеху!
                     🟢 🟢 😀 * 🏠      
            '''
            bot.send_message(message.chat.id, mess_win_without_friend_street1, reply_markup=markup)

#----------------------------------------------------------------------------------------------------------
    if message.text == "Идем на 3 улицу! Ура!":
        bot.send_message(message.chat.id, "Ты на третьей улице")
        mess_about_item = '''Ты видишь неопознанный предмет
                        Поднять его?
                        Да/Нет
                        '''
        markup = types.ReplyKeyboardMarkup()
        btn_pickup_yes = types.KeyboardButton('Да, поднять 2 предмет')
        btn_pickup_no = types.KeyboardButton('Нет, не буду поднимать 2 предмет')
        markup.row(btn_pickup_yes, btn_pickup_no)
        bot.send_message(message.chat.id, mess_about_item, reply_markup=markup)
    if message.text == "Да, поднять 2 предмет":
        items_list = ["Номер Друга", "Боржоми", "Бутылка Пива", "Бутылка водки"]
        item = random.choice(items_list)
        if item == "Номер Друга":
            bot.send_message(message.chat.id, "Тебе выпал номер друга! Он поможет провести тебя через улицу. Твои шансы 60%")
            move_chance_friend = random.randint(1, 10) <= 6
            if move_chance_friend == False:
                markup = types.ReplyKeyboardMarkup()
                btn1 = types.KeyboardButton("Поехали")
                markup.row(btn1)
                mess = ''' 
                        Упс, неповезло. Давай по новой
                        😀 * * * * 🏠
                    '''
                bot.send_message(message.chat.id, mess, reply_markup=markup)
            if move_chance_friend:
                markup = types.ReplyKeyboardMarkup()
                btn_next2 = types.KeyboardButton("Идем на 4 улицу! Ура!")
                markup.row(btn_next2)
                mess_win_with_friend_street1 = ''' 
                        Ура, ты прошел улицу!!!
                        🟢 🟢 🟢 😀 🏠
                    '''
                bot.send_message(message.chat.id, mess_win_with_friend_street1, reply_markup=markup)
        elif item == "Боржоми":
            bot.send_message(message.chat.id, '''Вау! Ты нашел бутылку Боржоми! Твои шансы пройти улицу 100% 
                                                                    Определнно - ты везунчик!  ''')
            move_chance_borjomi = random.randint(1, 100) <= 100
            if move_chance_borjomi:
                markup = types.ReplyKeyboardMarkup()
                btn_next2 = types.KeyboardButton("Идем на 4 улицу! Ура!")
                markup.row(btn_next2)
                mess_win_with_friend_street1 = ''' 
                        Ура, ты прошел улицу!!!
                        🟢 🟢 🟢 😀 🏠
                    '''
                bot.send_message(message.chat.id, mess_win_with_friend_street1, reply_markup=markup)
        elif item == "Бутылка Пива":
            bot.send_message(message.chat.id, "Ты нашел бутылку пива. Ой ой праздник продолжается... Твой шанс пройти улицу равен 40%")
            move_chance_pivo = random.randint(1, 10) <= 4
            if move_chance_pivo == False:
                markup = types.ReplyKeyboardMarkup()
                btn1 = types.KeyboardButton("Поехали")
                markup.row(btn1)
                mess = ''' 
                        Упс, неповезло. Давай по новой
                        😀 * * * * 🏠
                    '''
                bot.send_message(message.chat.id, mess, reply_markup=markup)
            if move_chance_pivo:
                markup = types.ReplyKeyboardMarkup()
                btn_next2 = types.KeyboardButton("Идем на 4 улицу! Ура!")
                markup.row(btn_next2)
                mess_win_with_friend_street1 = ''' 
                        Ура, ты прошел улицу!!!
                    🟢 🟢 🟢 😀 🏠
                    '''
                bot.send_message(message.chat.id, mess_win_with_friend_street1, reply_markup=markup)
        elif item == "Бутылка водки":
            bot.send_message(message.chat.id, "Тебе выпала бутылка водки... Ой ой... Это было зряяя. Твой шанс пройти улицу равен 10%")
            move_chance_vodka = random.randint(1, 10) >= 10
            if move_chance_vodka == False:
                markup = types.ReplyKeyboardMarkup()
                btn1 = types.KeyboardButton("Поехали")
                markup.row(btn1)
                mess = ''' 
                        Упс, неповезло. Давай по новой
                        😀 * * * * 🏠
                    '''
                bot.send_message(message.chat.id, mess, reply_markup=markup)
            if move_chance_vodka:
                markup = types.ReplyKeyboardMarkup()
                btn_next2 = types.KeyboardButton("Идем на 4 улицу! Ура!")
                markup.row(btn_next2)
                mess_win_with_friend_street1 = ''' 
                        Ура, ты прошел улицу!!!
                    🟢 🟢 🟢 😀 🏠
                    '''
                bot.send_message(message.chat.id, mess_win_with_friend_street1, reply_markup=markup)
    if message.text == "Нет, не буду поднимать 2 предмет":
        move_chance_without_1_item = random.randint(1, 2) >= 2
        if move_chance_without_1_item == False:
            markup = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("Поехали")
            markup.add(btn1)
            mess_loose_without_item_street2 =  ''' Упс, неповезло. Давай по новой
                        😀 * * * * 🏠
                    '''
            bot.send_message(message.chat.id, mess_loose_without_item_street2, reply_markup=markup)
        if move_chance_without_1_item:
            markup = types.ReplyKeyboardMarkup()
            btn1_win = types.KeyboardButton('Идем на 4 улицу! Ура!')
            markup.add(btn1_win)
            mess_win_without_item_street2 = ''' Ты на шаг ближе к успеху!
                    🟢 🟢 🟢 😀 🏠      
                '''
            bot.send_message(message.chat.id, mess_win_without_item_street2, reply_markup=markup)

#----------------------------------------------------------------------------------------------------------
    if message.text == "Идем на 4 улицу! Ура!":
        bot.send_message(message.chat.id, "Ты на четвёртой улице. Это последняя улица до твоего дома, соберись!")
        mess_about_item = '''Ты видишь неопознанный предмет
                        Поднять его?
                        Да/Нет
                        '''
        markup = types.ReplyKeyboardMarkup()
        btn_pickup_yes = types.KeyboardButton('Да, поднять 3 предмет')
        btn_pickup_no = types.KeyboardButton('Нет, не буду поднимать 3 предмет')
        markup.row(btn_pickup_yes, btn_pickup_no)
        bot.send_message(message.chat.id, mess_about_item, reply_markup=markup)
    if message.text == "Да, поднять 3 предмет":
        items_list = ["Номер Друга", "Боржоми", "Бутылка Пива", "Бутылка водки"]
        item = random.choice(items_list)
        if item == "Номер Друга":
            bot.send_message(message.chat.id, "Тебе выпал номер друга! Он поможет провести тебя через улицу. Твои шансы 60%")
            move_chance_friend = random.randint(1, 10) <= 6
            if move_chance_friend == False:
                markup = types.ReplyKeyboardMarkup()
                btn1 = types.KeyboardButton("Поехали")
                markup.row(btn1)
                mess = ''' 
                        Упс, неповезло. Давай по новой
                        😀 * * * * 🏠
                    '''
                bot.send_message(message.chat.id, mess, reply_markup=markup)
            if move_chance_friend:
                markup = types.ReplyKeyboardMarkup()
                btn_next2 = types.KeyboardButton("Ура, поздравляю. Ты дома!")
                markup.row(btn_next2)
                mess_win_with_friend_street3 = ''' 
                        Ура, ты дома!!!
                        🟢 🟢 🟢 🟢 🏠
                    '''
                bot.send_message(message.chat.id, mess_win_with_friend_street3, reply_markup=markup)
        elif item == "Боржоми":
            bot.send_message(message.chat.id, '''Вау! Ты нашел бутылку Боржоми! Твои шансы пройти улицу 100% 
                                                                        Определнно - ты везунчик!  ''')
            move_chance_borjomi = random.randint(1, 100) <= 100
            if move_chance_borjomi:
                markup = types.ReplyKeyboardMarkup()
                btn_next2 = types.KeyboardButton("Ура, поздравляю. Ты дома!")
                markup.row(btn_next2)
                mess_win_with_borjomi_street3 = ''' 
                            Ура, ты дома!!!
                            🟢 🟢 🟢 🟢 🏠
                        '''
                bot.send_message(message.chat.id, mess_win_with_borjomi_street3, reply_markup=markup)
        elif item == "Бутылка Пива":
            bot.send_message(message.chat.id, "Ты нашел бутылку пива. Ой ой праздник продолжается... Твой шанс пройти улицу равен 40%")
            move_chance_pivo = random.randint(1, 10) <= 4
            if move_chance_pivo == False:
                markup = types.ReplyKeyboardMarkup()
                btn1 = types.KeyboardButton("Поехали")
                markup.row(btn1)
                mess = ''' 
                        Упс, неповезло. Давай по новой
                        😀 * * * * 🏠
                    '''
                bot.send_message(message.chat.id, mess, reply_markup=markup)
            if move_chance_pivo:
                markup = types.ReplyKeyboardMarkup()
                btn_next2 = types.KeyboardButton("Ура, поздравляю. Ты дома!")
                markup.row(btn_next2)
                mess_win_with_pivo_street3 = ''' 
                        Ура, ты дома!!!
                        🟢 🟢 🟢 🟢 🏠
                    '''
                bot.send_message(message.chat.id, mess_win_with_pivo_street3, reply_markup=markup)
        elif item == "Бутылка водки":
            bot.send_message(message.chat.id, "Тебе выпала бутылка водки... Ой ой... Это было зряяя. Твой шанс пройти улицу равен 10%")
            move_chance_vodka = random.randint(1, 10) >= 10
            if move_chance_vodka == False:
                markup = types.ReplyKeyboardMarkup()
                btn1 = types.KeyboardButton("Поехали")
                markup.row(btn1)
                mess = ''' 
                        Упс, неповезло. Давай по новой
                        😀 * * * * 🏠
                    '''
                bot.send_message(message.chat.id, mess, reply_markup=markup)
            if move_chance_vodka:
                markup = types.ReplyKeyboardMarkup()
                btn_next2 = types.KeyboardButton("Ура, поздравляю. Ты дома!")
                markup.row(btn_next2)
                mess_win_with_vodka_street3 = ''' 
                        Ура, дома!!!
                    🟢 🟢 🟢 🟢 🏠
                    '''
                bot.send_message(message.chat.id, mess_win_with_vodka_street3, reply_markup=markup)
    if message.text == "Нет, не буду поднимать 3 предмет":
            move_chance_without_1_item = random.randint(1, 2) >= 2
            if move_chance_without_1_item == False:
                markup = types.ReplyKeyboardMarkup()
                btn1 = types.KeyboardButton("Поехали")
                markup.add(btn1)
                mess_loose_without_item_street4 =  ''' Упс, неповезло. Давай по новой
                            😀 * * * * 🏠
                        '''
                bot.send_message(message.chat.id, mess_loose_without_item_street4, reply_markup=markup)
            if move_chance_without_1_item:
                markup = types.ReplyKeyboardMarkup()
                btn1_win = types.KeyboardButton("Ура, поздравляю. Ты дома!")
                markup.add(btn1_win)
                mess_win_without_item_street4 = ''' 
                        Ура, дома!!!
                    🟢 🟢 🟢 🟢 🏠
                    '''
                bot.send_message(message.chat.id, mess_win_without_item_street4, reply_markup=markup)
    if message.text == "Ура, поздравляю. Ты дома!":
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton("Поехали")
        markup.add(btn1)
        mess = "Вот и все, ты дома! Надеюсь тебе понравилось! Хочешь еще раз?"
        bot.send_message(message.chat.id, mess, reply_markup=markup)
        


@bot.message_handler()
def OtherWords(message):
    """ Функция отслеживает команды, которые введены с клавиатуры"""

    start = "Начало"
    hello = "Привет"
    if message.text == start.lower() or message.text == hello.lower():
        bot.send_message(message.chat.id, "Привет! введи команду \"/start\", чтобы начать.")

#команда, чтобы бот работал все время, пока мы вручную его не отключим в терминале 
bot.polling(non_stop=True)