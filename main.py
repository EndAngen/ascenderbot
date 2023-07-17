from aiogram import Bot, executor, Dispatcher, types


TOKEN_API = "6346166669:AAGM-L0UdbEucjqgBbpQDGerwAhB28Pw35Y"

HELP_COMMAND = """
/help - список команд
/start - начать работать"""


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands=['help'])
async def help_command(massage: types.Message):
    await massage.reply(text=HELP_COMMAND)

@dp.message_handler(commands=['start'])
async def help_command(massage: types.Message):
    await massage.answer(text= "Welcome to Ascender team")
    await massage.delete()

if __name__ == "__main__":
    executor.start_polling(dp)