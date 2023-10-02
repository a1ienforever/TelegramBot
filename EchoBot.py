from aiogram import Bot, Dispatcher, executor, types

TOKEN_API = '6321893220:AAGWvVcojHfLU_mso_MGKTMzWNwtCss3Ctc'

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


def on_startup():
    print('Bot started')


@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Hello!')


@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=message.text)


if __name__ == '__main__':
    executor.start_polling(dp,on_startup=on_startup())