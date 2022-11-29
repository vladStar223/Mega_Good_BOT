from ast import Global
from cgitb import handler
from email.headerregistry import ContentTypeHeader
from mailbox import Message
from pickle import FALSE
import sqlite3
import telebot
from html.entities import codepoint2name
from lzma import CHECK_CRC64
import math
from stringprep import c22_specials, c6_set
from tkinter import LAST
import sys
import pathlib
from aiogram import types
from telebot import types
bot = telebot.TeleBot('5535707405:AAF0s7ZjQa5QY3PqIZWiiDhzPcH0hNyNtpc');
print('hello')
def gcd(a,b):
    pass
def normal(message):
    connect = sqlite3.connect('user.db')
    cursor = connect.cursor()
    mess = message.chat.id
    calculator = "0"
    cursor.execute(f"UPDATE login_id SET calculator =? WHERE id = ?", (calculator,mess)) 
    connect.commit()
@bot.message_handler(commands=['ds'])
def start_message(message):
   connect = sqlite3.connect('user.db')
   cursor = connect.cursor()
   cursor.execute(""" CREATE TABLE IF NOT EXISTS login_id(
      login_number PRIMARY KEY AUTOINCREMENT ,name TEXT
  )""")
   connect.commit()
   num = 1
   name = "Vlad"
   cursor.execute(f"UPDATE login_id SET name=? WHERE login_number = ?", (name,num)) 
   connect.commit()
   bot.send_message(message.chat.id,"33")
@bot.message_handler(commands=['start'])
def start_message(message):
   bot.send_message(message.chat.id,"222")
   connect = sqlite3.connect('user.db')
   cursor = connect.cursor()
   cursor.execute(""" CREATE TABLE IF NOT EXISTS login_id(
      login_number PRIMARY KEY AUTOINCREMENT , id INTEGER,name TEXT,surname TEXT,username TEXT, calculator TEXT
  )""")
   connect.commit()
   people_id = message.chat.id
   cursor.execute(f"SELECT id FROM login_id WHERE id = {people_id}")
   ###
   data = cursor.fetchone()
   if data is None:

      user_id = message.chat.id
      user_name = message.from_user.first_name
      user_surname = message.from_user.last_name
      username=message.from_user.username
      number = cursor.execute (f"SELECT * FROM login_id  ORDER BY name DESC LIMIT 1;")
      #bot.send_message(message.chat.id,number)
      #cursor.execute (f"UPDATE login_id SET name = 'Kukuruza228' WHERE number = '1'");
      calculator = "0"
      cursor.execute('INSERT INTO login_id  (id, name,surname, username,calculator) VALUES (?, ?, ?, ?,?)', (user_id, user_name, user_surname, username,calculator))
      connect.commit()
   else:
       bot.send_message(message.chat.id,'user be')
   #mess =cursor.execute( f"SELECT name  FROM login_id  WHERE = '3' ")
   #bot.send_message(message.chat.id,mess)
   markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
   bth0 = types.KeyboardButton("Режим калькулятор")
   bth01 = types.KeyboardButton("Режим  Задачи и Теория")
   markup.add(bth0, bth01)
   bot.send_message(message.chat.id, text="Режимы", reply_markup=markup)



@bot.message_handler(commands=['help'])
def start_message(message):
    connect = sqlite3.connect('user.db')
    cursor = connect.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS login_id(
     a TEXT 
  )""")
    connect.commit()
    a = "3443"
    b = 0
    c = 2
    d = 4
    iduser = message.chat.id
    cursor.execute(f"UPDATE login_id SET a=? WHERE id = ?", (a,iduser)) 
    connect.commit()








@bot.message_handler(content_types=['text'])
def func(message):

    connect = sqlite3.connect('user.db')
    cursor = connect.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS login_id(
    login_number PRIMARY KEY AUTOINCREMENT , id INTEGER,name TEXT,surname TEXT,username TEXT, calculator TEXT, a TEXT, b TEXT, c TEXT
  )""")
    connect.commit()
    mess = message.chat.id
    m = cursor.execute(f"SELECT calculator  FROM login_id WHERE id = {mess}").fetchone()
    #bot.send_message(message.chat.id,m)
    if(message.text == "квадратные уравнения вариант 1"):
        
        mess = message.chat.id
        calculator = "u1"
        cursor.execute(f"UPDATE login_id SET calculator =? WHERE id = ?", (calculator,mess)) 
        connect.commit()
        bot.send_message(message.chat.id,"Напишите в таком формате уравнение ( +-ax^2+-bx-+c)")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="Пишите", reply_markup=markup)
    elif(message.text == "квадратные уравнения вариант 2"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Ввод переменных")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, back)
        bot.send_message(message.chat.id, text="2", reply_markup=markup)
    elif(message.text == "214124215654654"):
        pass
    elif(message.text == "приветкнопки"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bt0 = types.KeyboardButton("0")
        bt1 = types.KeyboardButton("1")
        bt2 = types.KeyboardButton("2")
        bt3 = types.KeyboardButton("3")
        bt4 = types.KeyboardButton("4")
        bt5 = types.KeyboardButton("5")
        bt6 = types.KeyboardButton("6")
        bt7 = types.KeyboardButton("7")
        bt8 = types.KeyboardButton("8")
        bt9 = types.KeyboardButton("9")
        btm = types.KeyboardButton("-")
        btp = types.KeyboardButton("+")
        btv = types.KeyboardButton("Ввод")
        markup.add(bt0,bt1,bt2,bt3,bt4,bt5,bt6,bt7,bt8,bt9,btm,btp,btv)
        bot.send_message(message.chat.id, text="И", reply_markup=markup)
    elif message.text == "Ввод переменных":
        mess = message.chat.id
        calculator = "u2"
        cursor.execute(f"UPDATE login_id SET calculator =? WHERE id = ?", (calculator,mess)) 
        connect.commit()
        bot.send_message(message.chat.id,"Напишите в таком формате уравнение ( +-ax^2+-bx-+c)")
        bot.send_message(message.chat.id,"Водите отдельно каждое значение перед иксом")
        a = 'x'
        mess = message.chat.id
        cursor.execute(f"UPDATE login_id SET a =? WHERE id = ?", (a,mess)) 
        connect.commit()
        b = 'x'
        cursor.execute(f"UPDATE login_id SET b =? WHERE id = ?", (b,mess)) 
        connect.commit()
        c = 'x'
        cursor.execute(f"UPDATE login_id SET c =? WHERE id = ?", (c,mess)) 
        connect.commit()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="Пишите", reply_markup=markup)
    elif (message.text == "Квадратные уравнения"):
        pass
    elif (message.text == "Вернуться в главное меню"):
        normal(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("квадратные уравнения вариант 1")
        button2 = types.KeyboardButton("квадратные уравнения вариант 2")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "Режим калькулятор"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn11 = types.KeyboardButton(" квадратные уравнения вариант 1 ")
        btn22 = types.KeyboardButton("квадратные уравнения вариант 2 ")
        markup.add(btn11, btn22)
        bot.send_message(message.chat.id, text="Уравнения", reply_markup=markup)
    elif (message.text == "Режим  Задачи и Теория"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn11 = types.KeyboardButton(" В Разработке ")
        btn22 = types.KeyboardButton("В разработке ")
        markup.add(btn11, btn22)
        bot.send_message(message.chat.id, text="-", reply_markup=markup)
    elif (m[0] == "u1"):
        h = message.text
        l = len(h)
        le = 0
        n =0
        n1=0
        while l !=n:
         if h[n]=='x' and h[n+1] == '^' and h[n+2]=='2':
           le = n
         n= n+1
        i=le+3
        while l!=i:
           if h[i] !='x':
             n1=n1+1
             i = i+1
           else:
             i = l
        i = 1
        a =""
        while i!=le:
          a = h[i] + a
          i = 1+i
        i = le+3
        b = ""
        while i!= l-(l-le-n1-3):
         b = h[i] + b
         i = 1+i
        c=""
        i = le+n1+3
        while i!=l:
          c = h[i] + c
          i = i+1
        a= sorted (a)
        b = sorted (b)
        c = sorted (c)
        a = ''.join(a)
        b= ''.join(b)
        c= ''.join(c)
        c = c.replace('x',' ')

        a = int(a)
        b = int(b)
        c=int(c)
        if h[0] == "-":
         a = a*-1
        if h[le+3] == "-":
         b =b*-1
        D = (b*b)-4*a*c
        if D==0:
          x = (-b)/(2*a)
          bot.send_message(message.from_user.id,"один корень уравнения")
          bot.send_message(message.from_user.id,x)
          bot.send_message(message.from_user.id,"Дискприменат равен")
          bot.send_message(message.from_user.id,D)
          bot.send_message(message.from_user.id,"если не понимайете напишите /help")
          mess = message.chat.id
          calculator = "0"
          cursor.execute(f"UPDATE login_id SET calculator =? WHERE id = ?", (calculator,mess)) 
          connect.commit()

        else:
          if D<0:
            bot.send_message(message.from_user.id,"Кореней нет,если не понимайете напишите /help")
            bot.send_message(message.from_user.id, "пишите на англиской клавиатуре ")
            mess = message.chat.id
            calculator = "0"
            cursor.execute(f"UPDATE login_id SET calculator =? WHERE id = ?", (calculator,mess)) 
            connect.commit()

          if D>0:
            x1 =  (-b + math.sqrt(D))/(2*a)
            x2 =  (-b - math.sqrt(D))/(2*a)
            bot.send_message(message.from_user.id,"Первый корень")
            bot.send_message(message.from_user.id,x1)
            bot.send_message(message.from_user.id,"Второй корень")
            bot.send_message(message.from_user.id,x2)
            bot.send_message(message.from_user.id,"Дискприменат равен")
            bot.send_message(message.from_user.id,D)
            bot.send_message(message.from_user.id,"если не понимайете напишите /help")
            mess = message.chat.id
            calculator = "0"
            cursor.execute(f"UPDATE login_id SET calculator =? WHERE id = ?", (calculator,mess)) 
            connect.commit()
    elif (m[0] == "u2"):
        mess = message.chat.id
        a = cursor.execute(f"SELECT a  FROM login_id WHERE id = {mess}").fetchone()
        b = cursor.execute(f"SELECT b  FROM login_id WHERE id = {mess}").fetchone()
        c = cursor.execute(f"SELECT c  FROM login_id WHERE id = {mess}").fetchone()
        print(c)
        if a == '...':
            pass
        elif a[0] == 'x' :
             a = message.text
             mess = message.chat.id
             cursor.execute(f"UPDATE login_id SET a =? WHERE id = ?", (a,mess)) 
             connect.commit()
        elif b[0] == 'x' :
             b = message.text
             mess = message.chat.id
             cursor.execute(f"UPDATE login_id SET b =? WHERE id = ?", (b,mess)) 
             connect.commit()
        elif c[0] == 'x' :
             c = message.text
             mess = message.chat.id
             cursor.execute(f"UPDATE login_id SET c =? WHERE id = ?", (c,mess)) 
             connect.commit()
        if a[0] != 'x' and b[0] != 'x' and  c[0] != 'x':
             a = int(a[0])
             b = int(b[0])
             c = int(c)
             D = (b*b)-4*a*c
             if D==0:
              x = (-b)/(2*a)
              bot.send_message(message.from_user.id,"один корень уравнения")
              bot.send_message(message.from_user.id,x)
              bot.send_message(message.from_user.id,"Дискприменат равен")
              bot.send_message(message.from_user.id,D)
              bot.send_message(message.from_user.id,"если не понимайете напишите /help")
              mess = message.chat.id
              calculator = "0"
              cursor.execute(f"UPDATE login_id SET calculator =? WHERE id = ?", (calculator,mess)) 
              connect.commit()
             else:
              if D<0:
                bot.send_message(message.from_user.id,"Кореней нет,если не понимайете напишите /help")
                bot.send_message(message.from_user.id, "пишите на англиской клавиатуре ")
                mess = message.chat.id
                calculator = "0"
                cursor.execute(f"UPDATE login_id SET calculator =? WHERE id = ?", (calculator,mess)) 
                connect.commit()

              if D>0:
                x1 =  (-b + math.sqrt(D))/(2*a)
                x2 =  (-b - math.sqrt(D))/(2*a)
                bot.send_message(message.from_user.id,"Первый корень")
                bot.send_message(message.from_user.id,x1)
                bot.send_message(message.from_user.id,"Второй корень")
                bot.send_message(message.from_user.id,x2)
                bot.send_message(message.from_user.id,"Дискприменат равен")
                bot.send_message(message.from_user.id,D)
                bot.send_message(message.from_user.id,"если не понимайете напишите /help")
                mess = message.chat.id
                calculator = "0"
                cursor.execute(f"UPDATE login_id SET calculator =? WHERE id = ?", (calculator,mess)) 
                connect.commit()
    elif (m[0] == "gcd"):
        pass
    else:
        bot.send_message(message.chat.id,"Проверьте написанние  ")


  
bot.polling(none_stop=True)