import asyncio

from aiogram import Bot, F, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from database import database
from keyboard import online, inline
from aiogram.methods import SendPhoto

token = "6860621453:AAEEeTKl67NTo-XgOFOie0oEJ1VNU7tfgNI"

bot = Bot(token)
dp = Dispatcher()
db = database("users.db")
