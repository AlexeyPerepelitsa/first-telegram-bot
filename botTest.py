
import telebot
import imaplib
import poplib
import subprocess
import sys
from telebot import types
TOKEN = '6362391788:AAFwSaOd6VriA692GY-bd03FwWBHY8lmvgk'
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, 'Привет, я бот!')

# Определение клавиатуры с командами
    keyboard = types.InlineKeyboardMarkup()
    button_Sanchizes = types.InlineKeyboardButton(text='Санчизес', callback_data='command_Sanchizes')
    button_Chinazes = types.InlineKeyboardButton(text='Чиназес', callback_data='command_Chinazes')
    button_Ultrasanchez = types.InlineKeyboardButton(text='Ультрасанчез', callback_data='command_Ultrasanchez')
    button_Androzes = types.InlineKeyboardButton(text='Андрозес', callback_data='command_Androzes')
    keyboard.add(button_Chinazes)
    keyboard.add(button_Sanchizes)
    keyboard.add(button_Ultrasanchez)
    keyboard.add(button_Androzes)
    # Добавление кнопок с командами на клавиатуру
    for command in available_commands:
        keyboard.add(types.InlineKeyboardButton(text=command['text'], url=command['url']))

    # Отправка клавиатуры пользователю
    bot.send_message(message.chat.id, 'Выберите команду:', reply_markup=keyboard)

# Обработчик команды /command1
@bot.callback_query_handler(func=lambda call: True)
def handle_inline_button(call):
    if call.data == 'command_Sanchizes':
        # Ваш код для обработки команды /Андрозес
        bot.send_message(call.message.chat.id, 'https://youtube.com/shorts/G30_cpMI2VE?si=RyD11hGpzfSL51Cl')
        pass
    
    if call.data == 'command_Chinazes':
        # Ваш код для обработки команды /Андрозес
        bot.send_message(call.message.chat.id, 'https://www.youtube.com/hashtag/%D1%87%D0%B8%D0%BD%D0%B0%D0%B7%D0%B5%D1%81')
        pass

    if call.data == 'command_Ultrasanchez':
        # Ваш код для обработки команды /Андрозес
        bot.send_message(call.message.chat.id, 'https://youtube.com/shorts/D4Jghhsppzo?si=MXAx2sbO8pwuH9Q-')
        pass
    if call.data == 'command_Androzes':
        # Ваш код для обработки команды /Андрозес
        bot.send_message(call.message.chat.id, 'https://youtube.com/shorts/5a_Q6mMYi7M?si=MjVx3iA_wKQ0NUb2')
        pass


# Обработчик команды /stop
@bot.message_handler(commands=['stop'])
def stop(message):
    # Отправка сообщения о завершении работы
    bot.send_message(message.chat.id, 'Бот остановлен.')
    # Остановка бота
    bot.stop_polling()

# Обработчик команды /update
@bot.message_handler(commands=['update'])
def update(message):
    # Отправка сообщения о начале обновления
    bot.send_message(message.chat.id, 'Обновление бота...')
    
    # Выполнение команды для перезапуска бота
    subprocess.Popen([sys.executable, 'botTest.py'])
    
    # Остановка текущего экземпляра бота
    bot.stop_polling()
    sys.exit()

# Список доступных команд
   
available_commands = [
    {'text': 'Андрозес - YouTube', 'url': 'https://youtube.com/shorts/5a_Q6mMYi7M?si=MjVx3iA_wKQ0NUb2'},
    {'text': 'Чиназес - YouTube', 'url': 'https://www.youtube.com/hashtag/%D1%87%D0%B8%D0%BD%D0%B0%D0%B7%D0%B5%D1%81'},
    {'text': 'Ультрасанчез - YouTube', 'url': 'https://youtube.com/shorts/D4Jghhsppzo?si=MXAx2sbO8pwuH9Q-'},
    {'text': 'Cанчизес - YouTube', 'url': 'https://youtube.com/shorts/G30_cpMI2VE?si=RyD11hGpzfSL51Cl'}
]



bot.polling()
