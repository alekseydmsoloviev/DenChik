from aiogram import Router, types
import openai
from datetime import datetime, timedelta
from ..config import load_config
from ..models import SessionLocal, Mantra, Reminder
from .reminders import schedule_reminder

router = Router()
config = load_config()
DEFAULT_MANTRA = 'Слушайте эту мантру каждый день: «Я спокоен и полон сил.»'


@router.message(lambda m: m.text and m.text.lower() == 'идёт генерация мантры...')
async def generate_mantra(message: types.Message, state: dict) -> None:
    if not state.get('answers_done'):
        return
    session = SessionLocal()
    # When no OpenAI API key is configured, use a predefined mantra as a stub
    text = DEFAULT_MANTRA
    # prompt = 'Создай вдохновляющую мантру на основе предыдущих ответов.'
    # response = openai.ChatCompletion.create(model='gpt-4', messages=[{'role': 'user', 'content': prompt}])
    # text = response.choices[0].message.content
    mantra = Mantra(topic_id=state['topic'].id, text=text, step_index=1)
    session.add(mantra)
    session.commit()
    session.refresh(mantra)
    await message.answer(f'Ваша мантра:\n{text}')
    reminder = Reminder(user_id=state['topic'].user_id, mantra_id=mantra.id, remind_at=datetime.utcnow() + timedelta(hours=24))
    session.add(reminder)
    session.commit()
    await schedule_reminder(message.bot, reminder)
