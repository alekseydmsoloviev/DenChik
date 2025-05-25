import asyncio
from datetime import datetime
from aiogram import Bot
from ..models import SessionLocal, Reminder


async def schedule_reminder(bot: Bot, reminder: Reminder) -> None:
    await asyncio.sleep((reminder.remind_at - datetime.utcnow()).total_seconds())
    session = SessionLocal()
    rem = session.get(Reminder, reminder.id)
    if rem and not rem.sent:
        await bot.send_message(rem.user.telegram_id, 'Удалось ли послушать мантру?')
        rem.sent = True
        session.commit()


async def reminder_loop(bot: Bot) -> None:
    while True:
        session = SessionLocal()
        due = session.query(Reminder).filter(Reminder.remind_at <= datetime.utcnow(), Reminder.sent.is_(False)).all()
        for rem in due:
            await bot.send_message(rem.user.telegram_id, 'Удалось ли послушать мантру?')
            rem.sent = True
        session.commit()
        await asyncio.sleep(60)
