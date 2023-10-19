from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from keyboards.task import edit_task
from handlers.task import EditTaskStep
from aiogram.fsm.context import FSMContext

task_editor_router = Router()


@task_editor_router.message(EditTaskStep.edit_title)
async def add_task(message: Message, state: FSMContext):
    await message.answer(f'✅ Задача <b>{message.text}</b> добавлена', reply_markup=edit_task(1))
    await state.clear()

