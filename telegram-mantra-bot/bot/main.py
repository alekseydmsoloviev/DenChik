import asyncio
from aiogram import Bot, Dispatcher
from .config import load_config
from .handlers import start, selection, socratic, gpt, reminders
from .handlers.reminders import reminder_loop

config = load_config()

bot = Bot(token=config.bot_token)
dp = Dispatcher()

state = {}

dp.include_router(start.router)
dp.include_router(selection.router)
dp.include_router(socratic.router)
dp.include_router(gpt.router)


async def main() -> None:
    asyncio.create_task(reminders.reminder_loop(bot))
    await dp.start_polling(bot, allowed_updates=['message', 'callback_query'], state=state)


if __name__ == '__main__':
    asyncio.run(main())
