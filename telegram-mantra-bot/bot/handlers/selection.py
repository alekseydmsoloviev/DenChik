from aiogram import Router, types
from aiogram.filters import CallbackQuery
from ..keyboards import (
    request_keyboard,
    diag_start_keyboard,
    negative_options_keyboard,
    neutral_options_keyboard,
    positive_options_keyboard,
)

router = Router()


@router.callback_query(CallbackQuery(data='has_request'))
async def has_request(query: types.CallbackQuery) -> None:
    await query.message.answer('Выберите способ ввода запроса:', reply_markup=request_keyboard())
    await query.answer()


@router.callback_query(CallbackQuery(data='explore_inside'))
async def explore(query: types.CallbackQuery) -> None:
    await query.message.answer(
        'Сначала самодиагностика. Готовы пройти?',
        reply_markup=types.InlineKeyboardMarkup(
            inline_keyboard=[[
                types.InlineKeyboardButton(
                    text='\U0001F9ED Пройти самодиагностику',
                    callback_data='start_diag'
                )
            ]]
        )
    )
    await query.answer()


@router.callback_query(CallbackQuery(data='start_diag'))
async def diag_start(query: types.CallbackQuery) -> None:
    await query.message.answer(
        'Что ты чаще всего ощущаешь в последнее время — внутри себя, в фоне?',
        reply_markup=diag_start_keyboard()
    )
    await query.answer()


@router.callback_query(CallbackQuery(data='diag_negative'))
async def diag_negative(query: types.CallbackQuery, state: dict) -> None:
    state['diag_type'] = 'negative'
    await query.message.answer(
        'Выберите более точное состояние:',
        reply_markup=negative_options_keyboard()
    )
    await query.answer()


@router.callback_query(CallbackQuery(data='diag_neutral'))
async def diag_neutral(query: types.CallbackQuery, state: dict) -> None:
    state['diag_type'] = 'neutral'
    await query.message.answer(
        'Выберите более точное состояние:',
        reply_markup=neutral_options_keyboard()
    )
    await query.answer()


@router.callback_query(CallbackQuery(data='diag_positive'))
async def diag_positive(query: types.CallbackQuery, state: dict) -> None:
    state['diag_type'] = 'positive'
    await query.message.answer(
        'Выберите более точное состояние:',
        reply_markup=positive_options_keyboard()
    )
    await query.answer()


OPTION_BLOCKS = {
    'opt_emotions_trouble': 'ЭМОЦИИ',
    'opt_selfcrit': 'САМООЦЕНКА',
    'opt_procrastination': 'ПОВЕДЕНИЕ',
    'opt_loneliness': 'ОТНОШЕНИЯ',
    'opt_apathy': 'СМЫСЛ',
    'opt_anger': 'ЭМОЦИИ',
    'opt_guilt': 'САМООЦЕНКА',
    'opt_unrest': 'ЭМОЦИИ',
    'opt_nofeel': 'ПОВЕДЕНИЕ',
    'opt_auto': 'ПОВЕДЕНИЕ',
    'opt_stuck': 'ПОВЕДЕНИЕ',
    'opt_unknown': 'САМООЦЕНКА',
    'opt_detached': 'СМЫСЛ',
    'opt_empty': 'СМЫСЛ',
    'opt_self': 'СМЫСЛ',
    'opt_beliefs': 'САМООЦЕНКА',
    'opt_changes': 'ЭМОЦИИ',
    'opt_observe': 'ПОВЕДЕНИЕ',
    'opt_dialog': 'ОТНОШЕНИЯ',
    'opt_support': 'СМЫСЛ',
    'opt_bias': 'ПОВЕДЕНИЕ',
}


@router.callback_query(CallbackQuery(lambda c: c.data in OPTION_BLOCKS))
async def diag_option(query: types.CallbackQuery, state: dict) -> None:
    state['diag_block'] = OPTION_BLOCKS[query.data]
    # Start socratic questions
    from .socratic import begin_questions
    await begin_questions(query, state)
