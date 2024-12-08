import phonenumbers
from phonenumbers import timezone, geocoder, carrier
import telebot

bot = telebot.TeleBot("7692626473:AAEgJxf5PS_RG0_geBIqP3V8UU1uKlzmwl8", parse_mode=None)

@bot.message_handler(commands=["start"])
def echo_welcome(message):
    answer = "Привет я бот который сделает небольшой пробив\nпросто дай мне его номер"
    bot.send_message(message.chat.id, answer)

@bot.message_handler(content_types=["text"])
def echo_num(message):
    phonenumber = phonenumbers.parse(message.text)
    carrier2 = carrier.name_for_number(phonenumber, "ru")
    region = geocoder.description_for_number(phonenumber, "ru")
    timezone1 = timezone.time_zones_for_number(phonenumber)
    valid = phonenumbers.is_valid_number(phonenumber)

    answer0 = bot.send_message(message.chat.id, carrier2)
    answer1 = bot.send_message(message.chat.id, timezone1)
    answer2 = bot.send_message(message.chat.id, region)
    if valid == True:
        bot.send_message(message.chat.id, "Номер Валидный")
    elif valid == False:
        bot.send_message(message.chat.id, "Номер не Валидный")

bot.infinity_polling()
