from aiogram import Router, types
from ..keyboards import request_keyboard

router = Router()


@router.callback_query(lambda c: c.data == 'has_request')
async def has_request(query: types.CallbackQuery) -> None:
    await query.message.answer('Выберите способ ввода запроса:', reply_markup=request_keyboard())
    await query.answer()


@router.callback_query(lambda c: c.data == 'explore_inside')
async def explore(query: types.CallbackQuery) -> None:
    await query.message.answer('Сначала самодиагностика. Готовы пройти?', reply_markup=types.InlineKeyboardMarkup(inline_keyboard=[[types.InlineKeyboardButton(text='\U0001F9ED Пройти самодиагностику', callback_data='start_diag')]]))
    await query.answer()
