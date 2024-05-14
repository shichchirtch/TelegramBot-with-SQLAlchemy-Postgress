from bot_base import session_marker, User
from random import randint
from sqlalchemy import select


async def insert_new_user_in_table(user_tg_id:int, name:str):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.id == user_tg_id))
        print('query =', query)
        needed_data = query.scalar()
        print('needed_data = ', needed_data)
        if not needed_data:
            secret_number = randint(6, 100)
            new_us = User(id=user_tg_id, user_name=name, secret_number=secret_number)
            session.add(new_us)
            await session.commit()

async def update_table(user_tg_id:int, us_number:int):
    """Функция обновляет таблицу users"""
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.id == user_tg_id))
        n = query.scalar()
        n.attempts -= 1 # декремент попыток
        if n.att_1 == 0:
            n.att_1 = us_number
        elif n.att_2 == 0:
            n.att_2 = us_number
        elif n.att_3 == 0:
            n.att_3 = us_number
        elif n.att_4 == 0:
            n.att_4 = us_number
        elif n.att_5 == 0:
            n.att_5 = us_number
        await session.commit()

async def check_attempts_lost_number(user_tg_id):
    '''Функция проверяет количество оставшихся попыток'''
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.id == user_tg_id))
        needed_data = query.scalar()
        print('\n\n\nneeded_data.attempts', needed_data.attempts)
        if needed_data.attempts == 1:
            return True
        return False

async def reset(user_tg_id):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.id == user_tg_id))
        n = query.scalar()
        n.attempts = 5
        n.att_1 = n.att_2 = n.att_3 = n.att_4 = n.att_5 = 0
        await session.commit()









