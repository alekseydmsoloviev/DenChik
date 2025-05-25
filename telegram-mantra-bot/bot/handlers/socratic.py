from aiogram import Router, types, F
from ..models import SessionLocal, User, Topic, Answer

router = Router()

QUESTIONS = [
    'Что вы чувствуете сейчас?',
    'Почему это важно для вас?',
    'Что будет, если это не изменить?',
    'Как вы обычно справляетесь с этим?',
    'Что хотели бы изменить?'
]


@router.callback_query(lambda c: c.data == 'start_diag')
async def start_diag(query: types.CallbackQuery, state: dict) -> None:
    state['topic'] = Topic(user_id=await User.id_by_telegram(query.from_user.id), title='Новая тема')
    session = SessionLocal()
    session.add(state['topic'])
    session.commit()
    session.refresh(state['topic'])
    state['q'] = 0
    await query.message.answer(QUESTIONS[0])
    await query.answer()


@router.message(F.text)
async def handle_answer(message: types.Message, state: dict) -> None:
    if 'topic' not in state:
        return
    session = SessionLocal()
    answer = Answer(
        topic_id=state['topic'].id,
        question_index=state['q'],
        answer_text=message.text
    )
    session.add(answer)
    session.commit()
    state['q'] += 1
    if state['q'] < len(QUESTIONS):
        await message.answer(QUESTIONS[state['q']])
    else:
        await message.answer('Спасибо за ответы! Идёт генерация мантры...')
        state['answers_done'] = True
