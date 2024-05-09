# -*-coding: utf-8 -*-
import os
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from commands.help import *

# bot init
bot = Bot(token='6860621453:AAEEeTKl67NTo-XgOFOie0oEJ1VNU7tfgNI')
dp = Dispatcher(bot)

# datebase
connect = sqlite3.connect("users.db")
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id BIGINT,
    skin_id INT,
    level INT,
    balance INT,
    bank BIGINT,
    deposit INT,
    bitkoin INT,
    Ecoins INT,
    energy INT,
    expe INT,
    games INT,
    user_name STRING,
    user_status STRING,
    deposit_status INT,
    rating INT,
    work INT,
    pet1 INT,
    pet2 INT,
    pet3 INT,
    pet4 INT,
    pet5 INT,
    pet6 INT,
    pet7 INT,
    pet8 INT,
    pet9 INT,
    pet10 INT,
    pet_name STRING,
    pet_hp INT,
    pet_eat INT,
    pet_mood INT,
    checking INT,
    checking1 INT,
    checking2 INT,
    checking3 INT,
    status_block STRING
)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS mine(
    user_id BIGINT,
    user_name STRING,
    iron INT,
    gold INT,
    diamonds INT,
    amethysts INT,
    aquamarine INT,
    emeralds INT,
    matter INT,
    plasma INT
)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS workshop(
    user_id BIGINT,
    user_name STRING,
    work_shop INT,
    workshop_c INT
)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS farm(
    user_id BIGINT,
    user_name STRING,
    linen INT,
    cotton INT
)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS property(
    user_id BIGINT,
    user_name STRING,
    have STRING,
    yacht INT,
    cars INT,
    plane INT,
    helicopter INT,
    house INT,
    phone INT,
    business INT,
    farm INT
)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS bot(
    chat_id INT,
    last_stavka INT
)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS bot_bonus(
    user_id INT,
    last_stavka INT
)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS bot_merii(
    user_id INT,
    last_stavka INT
)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS bot_work(
    user_id INT,
    last_stavka INT
)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS bot_craft(
    user_id INT,
    last_stavka INT
)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS ban_list(
    user_id INT,
    user_name STRING,
    Cause STRING
)
""")


# start command
@dp.message_handler(text=['Статистика бота','статистика бота'])
async def stats(message):
    await statics_fgm(message) 


handlers_folder = 'modules'
for filename in os.listdir(handlers_folder):
    if filename.endswith(".py") and filename != "__init__.py":
        module_name = filename[:-3]
        module = __import__(f"{handlers_folder}.{module_name}", fromlist=["register_handlers"])
        module.register_handlers(dp)


if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, on_startup=main, skip_updates=True)
