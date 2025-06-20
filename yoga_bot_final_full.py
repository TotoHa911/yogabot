
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = '7862512838:AAFTLbHVsylOGTawisvDZsvCs_6Vux5qX6E'

def start(update: Update, context: CallbackContext):
    text = (
        "добро пожаловать в наше пространство йоги и заботы 🧘‍♀️\n\n"
        "я помогу тебе сориентироваться 🌿\nвот что у нас есть:\n\n"
        "🧾 /navigation — все полезные темы\n"
        "📅 /schedule — где и когда практики\n"
        "📖 /guide — забирай бесплатный PDF “залог удачного дня”\n"
        "📬 /contacts — если есть вопрос\n\n"
        "если просто хочется почитать интересное, поболтать — заходи в чат 🤍 [основной чат](https://t.me/chatdorogakyoga/175)"
    )
    keyboard = [
        [InlineKeyboardButton("📌 Навигация", callback_data='navigation'), InlineKeyboardButton("📅 Расписание", callback_data='schedule')],
        [InlineKeyboardButton("📖 Гайд", callback_data='guide'), InlineKeyboardButton("📬 Контакты", callback_data='contacts')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(text, parse_mode='Markdown', reply_markup=reply_markup)

def navigation(update: Update, context: CallbackContext):
    text = (
        "внутри группы 🧭\n\n"
        "🧘‍♀️ /asanas — обсуждаем нюансы\n"
        "🌬 /pranayamas — дыхание и концентрация\n"
        "📚 /books — вдохновение из текста\n"
        "🔮 /astrology — про звёзды и предназначение\n"
        "☕️ /personal — истории из практики\n"
        "🎵 /music — делимся треками, достойными внимания\n\n"
        "выбирай самый интересный раздел 🌿"
    )
    update.callback_query.answer()
    update.callback_query.edit_message_text(text, parse_mode='Markdown')

def schedule(update: Update, context: CallbackContext):
    text = (
        "расписание практик 🧘‍♀️\n\n"
        "обновляется каждую неделю и всегда есть в закреплённом сообщении в канале.\n\n"
        "⚡️ следующая живая практика в воскресенье, в 10:00\n"
        "☁️ йога онлайн по запросу (напиши Кате)\n\n"
        "[Посмотреть расписание](https://t.me/chatdorogakyoga/176)"
    )
    update.callback_query.answer()
    update.callback_query.edit_message_text(text, parse_mode='Markdown')

def guide(update: Update, context: CallbackContext):
    text = (
        "📖 Забирай PDF-гайд «Залог удачного дня» — утренний комплекс, с которого приятно начать день ☀️\n\n"
        "[Скачать гайд](https://t.me/Doroga_k_Yoga/23)"
    )
    update.callback_query.answer()
    update.callback_query.edit_message_text(text, parse_mode='Markdown')

def contacts(update: Update, context: CallbackContext):
    text = (
        "📬 Контакты:\n\n"
        "Преподаватель: Екатерина Багина — @katekateri_na\n"
        "Администратор: Антон Наумов — @ANT0N_NAUM0V\n"
        "Главный канал: https://t.me/Doroga_k_Yoga"
    )
    update.callback_query.answer()
    update.callback_query.edit_message_text(text)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    from telegram.ext import CallbackQueryHandler
    dp.add_handler(CallbackQueryHandler(navigation, pattern='^navigation$'))
    dp.add_handler(CallbackQueryHandler(schedule, pattern='^schedule$'))
    dp.add_handler(CallbackQueryHandler(guide, pattern='^guide$'))
    dp.add_handler(CallbackQueryHandler(contacts, pattern='^contacts$'))

    print("Бот запущен!")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
