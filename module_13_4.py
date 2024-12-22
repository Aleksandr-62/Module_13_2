from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = "?????????????????????????????????"
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

 # message_handler - обработчик входящих сообщений
@dp.message_handler(commands = ["start"])                  # перехватывает определенные комады после "/"
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text = "Calories")
async def age(message):
    await message.answer("Введите свой возраст")
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост")
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес")
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def gender(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    # Упрощенный вариант формулы Миффлина-Сан Жеора:
    # для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;
    result = (10*int(data['weight'])+6.25*int(data['growth'])-5*int(data['age'])+5)
    await message.answer(f'Ваша норма калорий: {result} ккал в сутки (для мужчин)')
    await UserState.gender.set()
    await state.finish()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)