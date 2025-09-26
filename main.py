import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from environs import Env
from deep_translator import GoogleTranslator

# Environmentdan token olish
env = Env()
env.read_env()
TOKEN = env.str("TOKEN")

# Bot va Dispatcher
bot = Bot(TOKEN)
dp = Dispatcher()

# Start command
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Assalomu alaykum, {message.from_user.first_name}! 👋")

# Help command
@dp.message(Command("help", "test"))
async def help_command(message: Message):
    await message.answer(f"🤖 Hurmatli {message.from_user.first_name}, sizga qanday yordam bera olaman?")

# Echo + tarjima
@dp.message(F.text)
async def echo(message: Message):
    try:
        translated = GoogleTranslator(source="uz", target="en").translate(message.text)
        await message.answer(f"🇺🇿 {message.text}\n🇬🇧 {translated}")
    except Exception as e:
        await message.answer("❌ Tarjima qilishda xatolik yuz berdi.")

# Main
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
