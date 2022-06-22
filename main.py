import logging #логування
import requests #бібліотека запитів
from bs4 import BeautifulSoup as b #парсер
from aiogram import Bot, Dispatcher, executor, types #бібліотека для API
bot = Bot(token="5567319716:AAGIsGrkVlqF5JYIfLtQA9IBiCmrejbt6_c") #токен бота
dp = Dispatcher(bot) #змінна для виклику диспетчера бота
logging.basicConfig(level=logging.INFO) #логування

URL = 'https://lviv1256.com/wheretogo/top-20-mists-lvova-kudy-pity-za-novymy-emotsiiamy/' #змінна(посилання на сайт)


def parser(url):
    r = requests.get(url) #запит на сайт
    soup = b(r.text, 'html.parser') #отримання інформації з сайту
    karta = soup.find_all('strong') #фільтрація по вибраному параметру
    return [c.text for c in karta] #очистка від тегів


kartazaraz = parser(URL) #змінна(готова колекція)
del kartazaraz[0] #видалення зайвого елементу


@dp.message_handler(commands="start") #читає команду /start
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True) #кнопки в рядок
    buttons = ["Цікаві місця львова", "Не знаю"]
    keyboard.add(*buttons) #кнопки
    await message.answer("Вас вітає бот путівник, що вам потрібно?", reply_markup=keyboard) #відповідь бота


@dp.message_handler(lambda message: message.text == "Цікаві місця львова") #читає заданий текст
async def with_puree(message: types.Message):
    await message.reply("Для видачі одної з цікавин Львова напишіть (Нові емоції)", reply_markup=types.ReplyKeyboardRemove()) #відповідь + закриття кнопок на клавіатурі


@dp.message_handler(lambda message: message.text == "Не знаю") #читає заданий текст
async def without_puree(message: types.Message):
    await message.answer_photo('https://lkplev.com/uploads/filemanager/2018/03/8543dfb3f92011a1a8e508a6dddaa027.jpg') #відповідь(зображення)


@dp.message_handler(lambda message: message.text == "Нові емоції") #читає заданий текст
async def without_puree(message: types.Message):
    await message.reply(kartazaraz[0]) #видача 1 елементу колекції
    del kartazaraz[0] #видалення першого елементу колекції


if __name__ == "__main__": #запуск
    executor.start_polling(dp, skip_updates=True) #опитування Telegram + пропуск накопичених повідомлень