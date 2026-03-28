# -*- coding: utf-8 -*-

import os
import asyncio
import time
import logging
from telethon import TelegramClient, events
from telethon import sessions

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Получаем параметры из переменных окружения Replit (Secrets)
API_ID = int(os.getenv("API_ID", "29829466"))
API_HASH = os.getenv("API_HASH", "c95497b8e5c18c8c65ea53ee29320ba9")

# Целевой получатель — Избранное (Saved Messages)
TARGET = "me"   # можно также использовать await client.get_me()

# Ключевые слова для поиска
KEYWORDS = [
    "звукорежиссёр", "звукорежиссер", "звукорежиссура",
    "саунд-дизайн", "саунддизайн", "звуковой дизайн", "композитор",
    "музыка к видео", "озвучка", "дубляж", "закадровый", "чистка звука",
    "шумоподавление", "сведение", "мастеринг", "микширование", "звукомонтаж",
    "постпродакшн", "Foley", "синхронизация звука"
]

# Использование строки сессии (рекомендуется для Replit)
string_session = os.getenv("STRING_SESSION")
if string_session:
    client = TelegramClient(sessions.StringSession(string_session), API_ID, API_HASH)
    logger.info("Используется строковая сессия")
else:
    client = TelegramClient("session_replit", API_ID, API_HASH)
    logger.info("Используется файловая сессия")

# Обработчик новых сообщений
@client.on(events.NewMessage())
async def handler(event):
    await asyncio.sleep(0.1)
    message = event.message
    if not message or not message.text:
        return

    # Игнорируем сообщения старше 5 минут
    if time.time() - message.date.timestamp() > 300:
        return

    text_lower = message.text.lower()
    for keyword in KEYWORDS:
        if keyword.lower() in text_lower:
            try:
                chat = await event.get_chat()
                if hasattr(chat, 'username') and chat.username:
                    link = f"https://t.me/{chat.username}/{message.id}"
                else:
                    chat_id = chat.id
                    if chat_id < 0:
                        chat_id = str(chat_id)[4:]  # убираем "-100"
                    link = f"https://t.me/c/{chat_id}/{message.id}"

                logger.info(f"Найдено ключевое слово в сообщении: {link}")
                # Отправляем в Избранное
                await client.send_message(
                    TARGET,
                    f"{message.text}\n\nСсылка на сообщение: {link}"
                )
                logger.info(f"Сообщение отправлено в Избранное: {message.text[:100]}")
            except Exception as e:
                logger.error(f"Ошибка при обработке сообщения: {e}")
            break

# Основная функция запуска бота
async def run_bot():
    try:
        await client.start()
        logger.info("Бот запущен и слушает сообщения...")
        await client.run_until_disconnected()
    except Exception as e:
        logger.error(f"Ошибка в работе бота: {e}")
        raise
    finally:
        await client.disconnect()

# Главная функция с перезапуском при сбоях
async def main():
    while True:
        try:
            await run_bot()
        except Exception as e:
            logger.error(f"Критическая ошибка, перезапуск через 30 секунд: {e}")
            await asyncio.sleep(30)
        else:
            logger.info("Бот остановлен")
            break

if __name__ == "__main__":
    from keep_alive import keep_alive
    keep_alive()
    asyncio.run(main())
