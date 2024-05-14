from aiogram.filters import BaseFilter
from aiogram.types import Message


class DATA_IS_DIGIT(BaseFilter):
    async def __call__(self, message: Message):
        if message.text.isdigit() and 0 < int(message.text) < 100:
            return True
        return False