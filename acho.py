import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
tg_token = "7736168649:AAGnici9WFipSHS-KIiNFTB8hlPE08L1c80"

bot = Bot(token=tg_token)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply("Привет, дорогой хозяин ! Чем я могу помочь ?")

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
