from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def edit_task(task_id):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Редактировать название', callback_data=f'edit_task:{task_id}:edit_title')],
        [InlineKeyboardButton(text='Редактировать описание', callback_data=f'edit_task:{task_id}:edit_description')],
        [InlineKeyboardButton(text='Редактировать дедлайн', callback_data=f'edit_task:{task_id}:edit_deadline')],
        [InlineKeyboardButton(text='Главное меню', callback_data='start_menu')]
    ])

    return keyboard