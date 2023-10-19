from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.main_menu import back_to_main_menu
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

task_router = Router()


class EditTaskStep(StatesGroup):
    edit_title = State()
    edit_description = State()
    edit_deadline = State()


@task_router.callback_query(F.data == 'add_task')
async def add_task(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text('Введите название задачи', reply_markup=back_to_main_menu())
    await state.set_state(EditTaskStep.edit_title)
    await callback.answer()


@task_router.callback_query(F.data == 'my_tasks')
async def show_tasks(callback: CallbackQuery):
    await callback.message.edit_text('Список задач пуст', reply_markup=back_to_main_menu())
    await callback.answer()


@task_router.callback_query(F.data == 'report_tasks')
async def show_reports(callback: CallbackQuery):
    await callback.message.edit_text('Этот раздел в разработке...', reply_markup=back_to_main_menu())
    await callback.answer()
