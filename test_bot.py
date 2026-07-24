import os
import asyncio
from telegram import Bot

TOKEN = os.getenv("TELEGRAMTOKEN")
CHAT_ID = os.getenv("CHAT_ID")


async def main():
    bot = Bot(token=TOKEN)

    await bot.send_message(
        chat_id=CHAT_ID,
        text="✅ Bybit Smart Scanner działa!"
    )


asyncio.run(main())
