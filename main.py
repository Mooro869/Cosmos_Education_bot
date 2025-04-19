from aiogram import Bot, Dispatcher, types
from aiogram import executor

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
    await message.answer(text='Выберите интересующих вас космонавтов:', reply_markup=kb.astronauts_btn)


@dp.message_handler(text=['Спутники🛰️'])
async def satellites_command(message: types.Message):
    await message.answer(text='', reply_markup=kb.satellites_btn)


@dp.callback_query_handler(lambda x: x.data == "earth")
async def earth(callback_query: types.CallbackQuery):
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo=open(config.planet_dict.get('earth'), "rb"),
                         caption=config.EARTH_DESCRIPTION)


@dp.callback_query_handler(lambda x: x.data == "jupiter")
async def jupiter(callback_query: types.CallbackQuery):
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo=open(config.planet_dict.get('jupiter'), "rb"),
                         caption=config.JUPITER_DESCRIPTION)


@dp.callback_query_handler(lambda x: x.data == "mars")
async def mars(callback_query: types.CallbackQuery):
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo=open(config.planet_dict.get('mars'), "rb"),
                         caption=config.MARS_DESCRIPTION)


@dp.callback_query_handler(lambda x: x.data == "merkury")
async def merkury(callback_query: types.CallbackQuery):
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo=open(config.planet_dict.get('merkury'), "rb"),
                         caption=config.MERKURY_DESCRIPTION)


@dp.callback_query_handler(lambda x: x.data == "neptune")
async def neptune(callback_query: types.CallbackQuery):
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo=open(config.planet_dict.get('neptune'), "rb"),
                         caption=config.NEPTUN_DESCRIPTION)


@dp.callback_query_handler(lambda x: x.data == "plutonium")
async def plutonium(callback_query: types.CallbackQuery):
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo=open(config.planet_dict.get('plutonium'), "rb"),
                         caption=config.PLUTONIUM_DESCRIPTION)


@dp.callback_query_handler(lambda x: x.data == "saturn")
async def saturn(callback_query: types.CallbackQuery):
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo=open(config.planet_dict.get('saturn'), "rb"),
                         caption=config.SATURN_DESCRIPTION)


@dp.callback_query_handler(lambda x: x.data == "uran")
async def uran(callback_query: types.CallbackQuery):
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo=open(config.planet_dict.get('uran'), "rb"),
                         caption=config.URAN_DESCRIPTION)


@dp.callback_query_handler(lambda x: x.data == "venus")
async def venus(callback_query: types.CallbackQuery):
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo=open(config.planet_dict.get('venus'), "rb"),
                         caption=config.VENUS_DESCRIPTION)


@dp.callback_query_handler(lambda x: x.data == "gagarin")
async def venus(callback_query: types.CallbackQuery):
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo=open(config.astronauts_dict.get('gagarin'), "rb"),
                         caption=config.GAGARIN_DESCRIPTION)


@dp.callback_query_handler(lambda x: x.data == "leonov")
async def venus(callback_query: types.CallbackQuery):
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo=open(config.astronauts_dict.get('leonov'), "rb"),
                         caption=config.LEONOV_DESCRIPTION)


@dp.callback_query_handler(lambda x: x.data == "popovich")
async def venus(callback_query: types.CallbackQuery):
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo=open(config.astronauts_dict.get('popovich'), "rb"),
                         caption=config.POPOVICH_DESCRIPTION)


@dp.callback_query_handler(lambda x: x.data == "krikalev")
async def venus(callback_query: types.CallbackQuery):
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo=open(config.astronauts_dict.get('krikalev'), "rb"),
                         caption=config.KRIKALEV_DESCRIPTION)


@dp.callback_query_handler(lambda x: x.data == "solovev")
async def venus(callback_query: types.CallbackQuery):
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo=open(config.astronauts_dict.get('solovev'), "rb"),
                         caption=config.SOLOVEV_DESCRIPTION)


@dp.callback_query_handler(lambda x: x.data == "kornienko")
async def venus(callback_query: types.CallbackQuery):
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo=open(config.astronauts_dict.get('kornienko'), "rb"),
                         caption=config.KORNIENKO_DESCRIPTION)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
