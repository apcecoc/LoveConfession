__version__ = (1, 0, 0)

#             █ █ ▀ █▄▀ ▄▀█ █▀█ ▀
#             █▀█ █ █ █ █▀█ █▀▄ █
#              © Copyright 2024
#           https://t.me/apcecoc
#
# 🔒      Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# meta developer: @apcecoc
# scope: hikka_only
# scope: hikka_min 1.2.10
from .. import loader, utils
import asyncio
import random
from telethon.tl.types import Message

@loader.tds
class LoveConfessionMod(loader.Module):
    """Создает анимированные признания в любви через inline"""
    strings = {"name": "LoveConfession"}

    async def lovecmd(self, message: Message):
        """Использование: .love <имя> или просто .love"""
        
        args = utils.get_args_raw(message)
        name = args if args else "любимая"
        
        hearts = ["❤️", "🧡", "💛", "💚", "💙", "💜", "🤍", "🤎"]
        love_phrases = [
            f"Я люблю тебя, {name}!",
            f"Ты - моё всё, {name}!", 
            f"Ты делаешь меня счастливым, {name}!",
            f"Ты - мой свет, {name}!",
            f"Ты - моя радость, {name}!"
        ]

        async def love_animation():
            frames = []
            
            # Анимация сердец
            for _ in range(3):
                for heart in hearts:
                    frames.append(heart)
            
            # Анимация текста
            text = ""
            love_msg = random.choice(love_phrases)
            for char in love_msg:
                text += char
                frames.append(text)
            
            # Финальное сообщение
            final_frame = (
                f"╔══════════════════╗\n"
                f"   {love_msg}\n"
                f"╚══════════════════╝\n"
                f"     {random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}"
            )
            frames.append(final_frame)
            
            return frames

        frames = await love_animation()
        
        try:
            # Создаем inline-сообщение через бота
            await self.animate(
                message,
                frames,
                interval=0.5,
                inline=True
            )
        except Exception as e:
            await utils.answer(message, f"🚫 Ошибка: {str(e)}")