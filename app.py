import html
import os
import platform
import random
import time
import urllib
from subprocess import check_output
import keyboa
import requests
import telebot
from colorama import Back, Fore, Style

#logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.INFO, filename = u'mylog.log')

bot = telebot.TeleBot('1493251280:AAFLd-I1FxE4gck3f6gkcxsfTBhsnv_-iZs');#Даём токен.

admin = [709265248,1291659706,1876112232,870857109]#Айди чатов админов

#Переменные с фотографиями для комманды программист.
images1 = ["https://cdn.discordapp.com/attachments/709460453725569085/808993635848159312/3HeO_20210119084221.gif", 
            "http://forum.moonpw.ru/uploads/monthly_2020_12/dave_coding_dribbble.thumb.gif.2025dbd947fca0fa08ccc3cc54c21c94.gif",
            "https://avatars.mds.yandex.net/get-zen_doc/1712061/pub_5e8d925f98ac907803229422_5e8d9d015af0cc63093f230e/orig",
            "https://i.pinimg.com/originals/2c/b8/ab/2cb8ab4aa36fc040dc4c34f1b4e3ba33.gif",
            "https://raw.githubusercontent.com/gist/mahmudinm/47588cab5af928d2c8a2976d90216ea7/raw/88f20c9d749d756be63f22b09f3c4ac570bc5101/programming.gif"]

Res = Style.RESET_ALL 

BGreen = Back.GREEN
FGreen = Fore.GREEN

#Вывод о запуске
print(Fore.GREEN + "[INFO] BrevnoBot started!",Res)
print(Style.RESET_ALL)
print(FGreen + "Запуск на ", platform.system(),"Сетевое имя:", platform.node(),Res)
bot.send_message(709265248, "Бот запущен!✅")


#Функция команды /цит
def citat():
    response = requests.get('https://bash.im/random')
    if (response.status_code==200):
        ee=response.text
        quo=ee.split('<div class="quote__body">',1)
        ee=quo[1]
        quo=ee.split('</div>',1)
        ee=quo[0]
        ee=html.unescape(ee)
        ee=ee.replace('<br>',"\n")
        ee=ee.replace('<br />',"\n")
        ee=ee.strip()
        return ee



@bot.message_handler(content_types=['text', 'audio'])#Получаем сообщения
def get_text_messages(message): #Получаю сообщение
    if message.chat.id in admin :
        def if_mess(t,m):
            if message.text == t:
                bot.send_message(message.from_user.id,m)
        
        print(Fore.CYAN, "Сообщение: ", message.text,", Отправил пользователь:", message.from_user.username,Res)
        

        if message.text == "Привет":
            bot.send_message(message.from_user.id,text="Привет, ты кто такой? иди на х***дильник.")
            if_mess("Лох","1")
        if message.text.lower() == "красавчик":
            bot.send_message(message.from_user.id,text="ДА ты красавчик")
        elif message.text.startswith("/цит") or message.text.startswith("/citat"):
            bot.send_message(message.from_user.id, citat())
        elif message.text == "/os":
            f=os.popen('cat /etc/*-release')
            rd=f.read()
            bot.send_message(message.from_user.id,rd)
        elif message.text.lower().find("программист") != -1:
            bot.send_animation(message.from_user.id,random.choice(images1))
        elif message.text == "пидорас":
            bot.send_message(message.from_user.id,"Попався пидор!")
            bot.send_photo(message.from_user.id,"https://cdn.discordapp.com/attachments/709460453725569085/809003835279671317/maxresdefault.jpg")
        else : bot.send_message(message.from_user.id, f"Нету команды  {message.text}!")
    else : 
        bot.send_message(message.from_user.id, "У вас нет прав на выполнение этой команды!")
        print(Fore.RED + "[INFO] {message.from_user.id} access denied!",Res)
        print(Style.RESET_ALL)

bot.polling(none_stop=True, interval=0)
os.system("clear")
print("Бот остановлен платформа:",platform.system())
print(time.asctime())
bot.send_message(709265248, "Бот остановлен!❎")
