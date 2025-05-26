from aiogram import Router, types
from aiogram.filters import Command
from ..keyboards import start_keyboard
from ..models import get_or_create_user

router = Router()


@router.message(Command('start'))
async def cmd_start(message: types.Message) -> None:
    await get_or_create_user(message.from_user.id)
    await message.answer(
        'Добро пожаловать! У вас есть запрос?',
        reply_markup=start_keyboard()
    )
