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
gagarin = types.KeyboardButton('Юрий Гагарин', callback_data='gagarin')
leonov = types.KeyboardButton('Алексей Леонов', callback_data='leonov')
popovich = types.KeyboardButton('Геннадий Попович', callback_data='popovich')
krikalev = types.KeyboardButton('Сергей Крикалев', callback_data='krikalev')
solovev = types.KeyboardButton('Анатолий Соловьев', callback_data='solovev')
kornienko = types.KeyboardButton('Михаил Корниенко', callback_data='kornienko')
astronauts_btn.add(gagarin, leonov, popovich, krikalev, solovev, kornienko)

# Кнопки спутников
satellites_btn = types.InlineKeyboardMarkup(row_width=3)
sputnik1 = types.KeyboardButton('Спутник-1 (СССР, 1957 г.)', callback_data='sputnik1')
explorer1 = types.KeyboardButton('Эксплорер-1 (США, 1958 г.)', callback_data='explorer1')
vostok1 = types.KeyboardButton('Восток-1 (СССР, 1961 г.)', callback_data='vostok1')
habbl = types.KeyboardButton('Хаббл (США, 1990 г.)', callback_data='habbl')
gps = types.KeyboardButton('GPS IIR-1 (США, 1997 г.)', callback_data='gps')
satellites_btn.add(sputnik1, explorer1, vostok1, habbl, gps)
