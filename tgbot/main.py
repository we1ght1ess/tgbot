# -*- coding: utf-8 -*-
import telebot
import pandas as pd

TOKEN = '6169338679:AAGOyjud6ZV3VU-2_tRmhyNC2wabez_OUVU'
bot = telebot.TeleBot(TOKEN)

list =[]

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Привет! Я бот, который выводид необходимые данные из Excel файла\n/grops - выводит все названия групп\n/pi101 - выводит все личные номера студентов ПИ101\n/controll - выводит все формы контроля\n/god - вывод все года, по которым представленны данные\n/number - выводит все оценки студентов и оценки студентов из ПИ101")

@bot.message_handler(commands=['grops'])
def echo_message(message):
    data = pd.read_excel('lab_pi_101.xlsx')
    groups = data['Группа'].unique()
    groups_str = ', '.join(groups)
    bot.send_message(message.chat.id,  f"Номера всех групп: {groups_str}")

@bot.message_handler(commands=['pi101'])
def echo_message(message):
    data = pd.read_excel('lab_pi_101.xlsx')
    pi101 = data[data['Группа'] == "ПИ101"] 
    stud_pi = len(pi101['Личный номер студента'].unique())
    zachetki_pi = data.loc[data['Группа'] == 'ПИ101', 'Личный номер студента'].unique()
    zachetki_pi_str = ', '.join(map(str, zachetki_pi))
    bot.send_message(message.chat.id,  f"В датасете находятся оценки {stud_pi} студентов ПИ101 со следующими личными номерами: {zachetki_pi_str}")
    
@bot.message_handler(commands=['controll'])
def echo_message(message):
    data = pd.read_excel('lab_pi_101.xlsx')
    control = data['Уровень контроля'].unique() 
    control1 = ', '.join(map(str, control))
    bot.send_message(message.chat.id,  f"Используемые формы контроля: {control1}")

@bot.message_handler(commands=['god'])
def echo_message(message):
    data = pd.read_excel('lab_pi_101.xlsx')
    goda = data['Год'].unique() 
    goda_sorted = sorted(goda) 
    goda1 = ', '.join(map(str, goda_sorted)) 
    bot.send_message(message.chat.id,  f"Данные представлены по следующим учебным годам: {goda1}")

@bot.message_handler(commands=['number'])
def echo_message(message):
    data = pd.read_excel('lab_pi_101.xlsx')
    count = data.shape[0] 
    count1 =  data['Группа'].str.contains('ПИ101').sum()
    bot.send_message(message.chat.id,  f'В исходном датасете содержалось {count} оценок, из них {count1} оценок относятся к группе ПИ101')

if __name__ == '__main__':
    bot.polling(none_stop=True)
