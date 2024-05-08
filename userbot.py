from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Привет! Я бот для поиска ключевых слов. Просто отправь мне сообщение с текстом, который тебе интересен.")

def keyword_search(update: Update, context: CallbackContext) -> None:
    text = update.message.text.lower()
    keywords = ['звукорежиссер', 'пост', 'звукорежиссер пост', 'нужен звукорежиссер', 'пост прод', 'звукорежиссер нужен', 'саунд дизайн', 'нужен саунд дизайнер', 'саунд диз', 'нужен саунд дизайн' ]
    
    for keyword in keywords:
        if keyword in text:
            post_url = 'https://yourwebsite.com/post'  # Замените на реальную ссылку на пост с ключевым словом
            update.effective_user.send_message(f"Найдено ключевое слово: {keyword}\n{post_url}")

def main() -> None:
    updater = Updater('6826303809:AAE2an6RcnSV-a4ua_o3sYgRl2WBDXfSn7s', use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, keyword_search))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
