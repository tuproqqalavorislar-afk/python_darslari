import asyncio
from aiogram import Bot , Dispatcher,types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
TOKEN = ""
bot = Bot(token = TOKEN)
db = Dispatcher() 

kb=ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Bosh menyu")]],
    resize_keyboard=True
)

@db.message(Command("start"))
async def start_handler(message:types.Message):
    await message.answer("Bot ga xush kelibsiz",reply_markup=kb)

@db.message(Command("help"))
async def start_handler(message:types.Message):
    await message.answer("Nima yordam kerak❓")

# @db.message()
# async def msg(message:types.Message):
    

async def main():
    await db.start_polling(bot)

if __name__=="__main__":
    print("Bot ishga tushdi")
asyncio.run(main())