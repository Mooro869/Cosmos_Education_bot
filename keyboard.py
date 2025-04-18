from aiogram import types


# Кнопки при запуске бота
start_btn = types.ReplyKeyboardMarkup(resize_keyboard=True)
planet = types.KeyboardButton('Планеты🌘')
astronauts = types.KeyboardButton('Космонавты👨‍🚀')
satellites = types.KeyboardButton('Спутники🛰️')
start_btn.add(planet, astronauts, satellites)

# Кнопки планет
planet_btn = types.InlineKeyboardMarkup(row_width=3)
earth = types.KeyboardButton('Земля', callback_data='earth')
jupiter = types.KeyboardButton('Юпитер', callback_data='jupiter')
mars = types.KeyboardButton('Марс', callback_data='mars')
merkury = types.KeyboardButton('Меркурий', callback_data='merkury')
neptune = types.KeyboardButton('Нептун', callback_data='neptune')
plutonium = types.KeyboardButton('Плутон', callback_data='plutonium')
saturn = types.KeyboardButton('Сатурн', callback_data='saturn')
uran = types.KeyboardButton('Уран', callback_data='uran')
venus = types.KeyboardButton('Венера', callback_data='venus')
planet_btn.add(earth, jupiter, mars, merkury, neptune, plutonium, saturn, uran, venus)

# Кнопки астронавтов
astronauts_btn = types.InlineKeyboardMarkup(row_width=3)

astronauts_btn.add()

# Кнопки спутников
satellites_btn = types.InlineKeyboardMarkup(row_width=3)

satellites_btn.add()