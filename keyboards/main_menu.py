from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def render_main_menu():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Добавить задачу', callback_data='add_task')],
        [InlineKeyboardButton(text='Мои задачи', callback_data='my_tasks')],
        [InlineKeyboardButton(text='Отчёты', callback_data='report_tasks')]
    ])

    return keyboard


def back_to_main_menu():
    keyboard = InlineKeyboardMarkup(inline_keyboard=
                                    [[InlineKeyboardButton(text='Главное меню', callback_data='start_menu')]]
                                    )
    return keyboard