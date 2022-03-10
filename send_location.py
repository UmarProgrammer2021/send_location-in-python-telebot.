import telebot
from telebot import types

TOKEN='your token'
client=telebot.Telebot(TOKEN)

@client.message_handler(commands=['start'])
def start(message):
    interfeys=types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1=types.KeyboardButton('menu button')
    interfeys.add(button1,)
    
    myname = message.from_user.username

    client.send_message(message.chat.id,f'<b>Assalomu aleykum</b> @{myname}',parse_mode='HTML',reply_markup=interfeys)


@client.message_handler(content_types=['text'])
def menu(message):
    if message.text=='Aloqa📞':
        client.send_message(message.chat.id,"Hello World")
        client.send_location(message.chat.id,'place coordinates,coordinates')