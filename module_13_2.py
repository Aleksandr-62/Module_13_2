from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "???????????????????????????????????"
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

 # message_handler - обработчик входящих сообщений
@dp.message_handler(text = ["Urban", "HH", "Ты кто"])      # перехватывает определенные слова, фразы
async def urban_message(message):
    print('Urban message')

@dp.message_handler(commands = ["start"])                  # перехватывает определенные комады после "/"
async def start_message(message):
    print('Start message')

@dp.message_handler()                                      # перехватывает все осташие сообщения
async def all_message(message):
    print('Мы получили соообщение')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)