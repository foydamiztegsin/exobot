import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'Botingiz Tokenini joylashtirasiz!'

# Configure logging
logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum!\nUshbu bot bepul serverga yuklash maqsadida test uchun yozildi!")



@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
