from aiogram import Bot, Dispatcher, types
from aiogram import executor

import time

import config
import keyboard as kb

# @CosmosEducationbot
bot = Bot(token=config.TOKEN_API)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text=f"Здравствуй {message.from_user.full_name}!" + config.START_TEXT,
                         reply_markup=kb.start_btn)


@dp.message_handler(text=['Планеты🌘'])
async def planet_command(message: types.Message):
    await message.answer(text='Выберите интересующую вас планету:', reply_markup=kb.planet_btn)


@dp.message_handler(text=['Космонавты👨‍🚀'])
async def astronauts_command(message: types.Message):
    await message.answer(text='', reply_markup=kb.astronauts_btn)


@dp.message_handler(text=['Спутники🛰️'])
async def satellites_command(message: types.Message):
    await message.answer(text='', reply_markup=kb.satellites_btn)


@dp.callback_query_handler(lambda x: x.data == "earth")
async def earth(callback_query: types.CallbackQuery):
    ...


@dp.callback_query_handler(lambda x: x.data == "jupiter")
async def jupiter(callback_query: types.CallbackQuery):
    ...


@dp.callback_query_handler(lambda x: x.data == "mars")
async def mars(callback_query: types.CallbackQuery):
    ...


@dp.callback_query_handler(lambda x: x.data == "merkury")
async def merkury(callback_query: types.CallbackQuery):
    ...


@dp.callback_query_handler(lambda x: x.data == "neptune")
async def neptune(callback_query: types.CallbackQuery):
    ...


@dp.callback_query_handler(lambda x: x.data == "plutonium")
async def plutonium(callback_query: types.CallbackQuery):
    ...


@dp.callback_query_handler(lambda x: x.data == "saturn")
async def saturn(callback_query: types.CallbackQuery):
    ...


@dp.callback_query_handler(lambda x: x.data == "uran")
async def uran(callback_query: types.CallbackQuery):
    ...


@dp.callback_query_handler(lambda x: x.data == "venus")
async def venus(callback_query: types.CallbackQuery):
    ...


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
