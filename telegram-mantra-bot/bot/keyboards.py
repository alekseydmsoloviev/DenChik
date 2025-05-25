from aiogram import types


def start_keyboard() -> types.InlineKeyboardMarkup:
    keyboard = [
        [
            types.InlineKeyboardButton(text='\u270d\ufe0f Да, у меня есть запрос', callback_data='has_request')
        ],
        [
            types.InlineKeyboardButton(text='\ud83d\udd0e Хочу сначала разобраться…', callback_data='explore_inside')
        ]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=keyboard)


def request_keyboard() -> types.InlineKeyboardMarkup:
    keyboard = [
        [
            types.InlineKeyboardButton(text='\U0001F193 Написать текстом', callback_data='request_text')
        ],
        [
            types.InlineKeyboardButton(text='\U0001F5E3 Голосом (подписка)', callback_data='enable_voice')
        ]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=keyboard)
