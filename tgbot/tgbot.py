# -*- coding: utf-8 -*-
import telebot
import pandas as pd
import requests
import io 
from telebot import types

TOKEN = '6169338679:AAGOyjud6ZV3VU-2_tRmhyNC2wabez_OUVU' #@Stud212126_bot
bot = telebot.TeleBot(TOKEN)

data = None

@bot.message_handler(content_types=['document'])
def handle_docs(message):
    global data
    try:
        file_info = bot.get_file(message.document.file_id)
        file = requests.get('https://api.telegram.org/file/bot{}/{}'.format(TOKEN, file_info.file_path))

        data = pd.read_excel(io.BytesIO(file.content))

        expected_columns = ['Группа', 'Личный номер студента', 'Уровень контроля', 'Год']  

        for column in expected_columns:
            if column not in data.columns:
                raise ValueError(f"Произошла ошибка при загрузке файла, попробуйте снова.")

        bot.reply_to(message, "Файл успешно загружен!")
    except Exception as error:
        print(error)
        bot.reply_to(message, "Произошла ошибка при загрузке файла, попробуйте снова.")

list =[]
user_states = {}
current_group = 'ПИ101'
current_group_1 = "change_group"

@bot.message_handler(commands=['change_group'])
def change_group_command(message):
    user_states[message.chat.id] = current_group_1
    bot.send_message(message.chat.id, f"Введите название группы")

@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == current_group_1)
def change_group_set_name(message):
    global current_group
    current_group = message.text
    if current_group in data['Группа'].values:
        bot.send_message(message.chat.id, f"Текущая группа была успешно изменена на {current_group}")
        user_states[message.chat.id] = None
    else:
        bot.send_message(message.chat.id, f"Группа {current_group} не найдена в данных")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['/start','/change_group', '/grops', '/otchet', '/controll', '/god']])
    bot.send_message(message.chat.id, "Привет! Я бот, который выводит необходимые данные из Excel файла\n"
                    "\n⚠️ОБЯЗАТЕЛЬНО ЗАГРУЗИТE EXCEL ФАЙЛ ПЕРЕД ИСОЛЬЗОВАНИЕМ КОМАНД!\n "
                    "\n/change_group (группа) - изменить группу для отчета\n"
                    "/grops - выводит все названия групп\n"
                    "/otchet - выводит отчет по выбранной группе\n"
                    "/controll - выводит все формы контроля\n"
                    "/god - вывод все года, по которым представленны данные", reply_markup=keyboard)
    
@bot.message_handler(commands=['grops'])
def echo_message(message):
    groups = data['Группа'].unique()
    groups_str = ', '.join(groups)
    bot.send_message(message.chat.id,  f"Номера всех групп: {groups_str}")

@bot.message_handler(commands=['otchet'])
def echo_message(message):
    gr = data[data['Группа'] == current_group] 
    stud_pi = len(gr['Личный номер студента'].unique())
    zachetki_pi = data.loc[data['Группа'] == current_group, 'Личный номер студента'].unique()
    zachetki_pi_str = ', '.join(map(str, zachetki_pi))
    count = data.shape[0] 
    count1 =  data['Группа'].str.contains(current_group).sum()
    bot.send_message(message.chat.id,  f'В исходном датасете содержалось {count} оценок, из них {count1} оценок относятся к группе {current_group}')
    bot.send_message(message.chat.id,  f"В датасете находятся оценки {stud_pi} студентов {current_group} со следующими личными номерами: {zachetki_pi_str}")
    
@bot.message_handler(commands=['controll'])
def echo_message(message):
    control = data['Уровень контроля'].unique() 
    control1 = ', '.join(map(str, control))
    bot.send_message(message.chat.id,  f"Используемые формы контроля: {control1}")

@bot.message_handler(commands=['god'])
def echo_message(message):
    goda = data['Год'].unique() 
    goda_sorted = sorted(goda) 
    goda1 = ', '.join(map(str, goda_sorted)) 
    bot.send_message(message.chat.id,  f"Данные представлены по следующим учебным годам: {goda1}")

if __name__ == '__main__':
    bot.polling(none_stop=True)