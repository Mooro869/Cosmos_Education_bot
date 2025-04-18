from aiogram import Bot, Dispatcher, types
from aiogram import executor

import time

import config
import keyboard as kb

# @CosmosEducationbot
bot = Bot(token=config.TOKEN_API)
dp = Dispatcher(bot=bot)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
