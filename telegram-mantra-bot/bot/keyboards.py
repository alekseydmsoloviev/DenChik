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


def diag_start_keyboard() -> types.InlineKeyboardMarkup:
    keyboard = [
        [types.InlineKeyboardButton(text='\U0001F641 Негативное', callback_data='diag_negative')],
        [types.InlineKeyboardButton(text='\U0001F610 Нейтральное', callback_data='diag_neutral')],
        [types.InlineKeyboardButton(text='\U0001F9D8 Позитивное', callback_data='diag_positive')]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=keyboard)


def negative_options_keyboard() -> types.InlineKeyboardMarkup:
    keyboard = [
        [types.InlineKeyboardButton(text='\U0001F61F Тревожность, страх', callback_data='opt_emotions_trouble')],
        [types.InlineKeyboardButton(text='\U0001F61E Самокритика, «я не такой»', callback_data='opt_selfcrit')],
        [types.InlineKeyboardButton(text='\U0001F501 Прокрастинация, застревание', callback_data='opt_procrastination')],
        [types.InlineKeyboardButton(text='\U0001F494 Ощущение одиночества', callback_data='opt_loneliness')],
        [types.InlineKeyboardButton(text='\U0001F610 Апатия, пустота', callback_data='opt_apathy')],
        [types.InlineKeyboardButton(text='\U0001F620 Раздражение, гнев', callback_data='opt_anger')],
        [types.InlineKeyboardButton(text='\U0001F630 Стыд, вина', callback_data='opt_guilt')]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=keyboard)


def neutral_options_keyboard() -> types.InlineKeyboardMarkup:
    keyboard = [
        [types.InlineKeyboardButton(text='\U0001F301 Непонятное напряжение', callback_data='opt_unrest')],
        [types.InlineKeyboardButton(text='\U0001F636 «Ничего не чувствую»', callback_data='opt_nofeel')],
        [types.InlineKeyboardButton(text='\u23F3 Автоматизм, инерция', callback_data='opt_auto')],
        [types.InlineKeyboardButton(text='\U0001F914 Понять, в чём застрял', callback_data='opt_stuck')],
        [types.InlineKeyboardButton(text='\U0001F62C Что-то не так, но что?', callback_data='opt_unknown')],
        [types.InlineKeyboardButton(text='\U0001F9CD Живу рядом с собой', callback_data='opt_detached')],
        [types.InlineKeyboardButton(text='\U0001F937 «Вроде всё норм, но пусто»', callback_data='opt_empty')]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=keyboard)


def positive_options_keyboard() -> types.InlineKeyboardMarkup:
    keyboard = [
        [types.InlineKeyboardButton(text='\u2728 Хочу глубже понять себя', callback_data='opt_self')],
        [types.InlineKeyboardButton(text='\U0001F4A1 Пора пересмотреть установки', callback_data='opt_beliefs')],
        [types.InlineKeyboardButton(text='\U0001F331 В процессе перемен', callback_data='opt_changes')],
        [types.InlineKeyboardButton(text='\U0001F50D Наблюдаю за собой', callback_data='opt_observe')],
        [types.InlineKeyboardButton(text='\U0001F4AC Переформулировать диалог', callback_data='opt_dialog')],
        [types.InlineKeyboardButton(text='\U0001F9D8 Больше внутренней опоры', callback_data='opt_support')],
        [types.InlineKeyboardButton(text='\U0001F3AF Когнитивные ловушки', callback_data='opt_bias')]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=keyboard)
