from aiogram import F, Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from keyboards.main_menu import render_main_menu
from handlers.task import task_router
from handlers.task_edit import task_editor_router
import asyncio

dp = Dispatcher()
dp.include_routers(task_router, task_editor_router)


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Главное меню', reply_markup=render_main_menu())


@dp.callback_query(F.data == 'start_menu')
async def replace_by_main_menu(callback: CallbackQuery):
    await callback.message.edit_text('Главное меню', reply_markup=render_main_menu())


async def main():
    bot = Bot('6593111234:AAEJngbRnJXj_kbfQcSk9ShQ8BFH4I6b1iw', parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
