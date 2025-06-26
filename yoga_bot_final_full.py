from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = "7862512838:AAFTLbHVsylOGTawisvDZsvCs_6Vux5qX6E"

# Клавиатура под стартом
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        ["📌 Навигация", "📅 Расписание"],
        ["📖 Гайд", "📬 Контакты"]
    ],
    resize_keyboard=True
)

def start(update: Update, context: CallbackContext):
    text = (
        "добро пожаловать в наше пространство йоги и заботы 🧘‍♀️\n\n"
        "я помогу тебе сориентироваться 🌿\nвот что у нас есть:\n\n"
        "🧾 Навигация — все полезные темы\n"
        "📅 Расписание — где и когда практики\n"
        "📖 Гайд — забирай бесплатный PDF “залог удачного дня”\n"
        "📬 Контакты — если есть вопрос\n\n"
        "если просто хочется почитать интересное, поболтать — заходи в чат 🤍 [основной чат](https://t.me/chatdorogakyoga/175)"
    )
    update.message.reply_text(text, parse_mode='Markdown', reply_markup=keyboard)

def navigation(update: Update, context: CallbackContext):
    update.message.reply_text(
        "внутри группы 🧭\n\n"
        "🧘‍♀️ [асаны в деталях](https://t.me/chatdorogakyoga/177) — обсуждаем нюансы\n"
        "🌬 [пранаямы](https://t.me/chatdorogakyoga/185) — дыхание и концентрация\n"
        "📚 [книги](https://t.me/chatdorogakyoga/187) — вдохновение из текста\n"
        "🔮 [астрология](https://t.me/chatdorogakyoga/225) — про звёзды и предназначение\n"
        "☕️ [о личном](https://t.me/chatdorogakyoga/191) — истории из практики\n"
        "🎵 [музыка](https://t.me/chatdorogakyoga/189) — делимся треками, достойными внимания\n\n"
        "выбирай самый интересный раздел 🌿",
        parse_mode='Markdown'
    )

def schedule(update: Update, context: CallbackContext):
    update.message.reply_text(
        "расписание практик 🧘‍♀️\n\n"
        "обновляется каждую неделю и всегда есть в закреплённом сообщении в канале.\n\n"
        "⚡️ следующая живая практика в воскресенье, в 10:00\n"
        "☁️ йога онлайн по запросу (напиши Кате)\n\n"
        "[Посмотреть расписание](https://t.me/chatdorogakyoga/176)",
        parse_mode='Markdown'
    )

def guide(update: Update, context: CallbackContext):
    update.message.reply_text(
        "📖 Забирай PDF-гайд «Залог удачного дня» — утренний комплекс, с которого приятно начать день ☀️\n\n"
        "[Скачать гайд](https://t.me/Doroga_k_Yoga/23)",
        parse_mode='Markdown'
    )

def contacts(update: Update, context: CallbackContext):
    update.message.reply_text(
        "📬 Контакты:\n\n"
        "Преподаватель: Екатерина Багина — @katekateri_na\n"
        "Администратор: Антон Наумов — @ANT0N_NAUM0V\n"
        "Главный канал: https://t.me/Doroga_k_Yoga"
    )

# Дополнительные команды по навигации
def asanas(update: Update, context: CallbackContext):
    update.message.reply_text(
        "🤸‍♀️ асаны в деталях\n\n"
        "здесь мы разбираем позы — ведь грамотное их выполнение и есть польза и бережное отношение к телу 🤍\n\n"
        "[Перейти в раздел](https://t.me/chatdorogakyoga/177)",
        parse_mode='Markdown'
    )

def pranayamas(update: Update, context: CallbackContext):
    update.message.reply_text(
        "🌬 пранаямы: суть и практика\n\n"
        "здесь мы говорим о дыхании — простом, но самом могучем инструменте.\n"
        "если сложно медитировать — начни с пранаямы 💨\n\n"
        "[Перейти в раздел](https://t.me/chatdorogakyoga/185)",
        parse_mode='Markdown'
    )

def meditations(update: Update, context: CallbackContext):
    update.message.reply_text(
        "🎧 коллекция медитаций\n\n"
        "медитации под разное настроение — расслабиться, сфокусироваться, услышать себя.\n\n"
        "[Перейти в раздел](https://t.me/chatdorogakyoga/183)",
        parse_mode='Markdown'
    )

def books(update: Update, context: CallbackContext):
    update.message.reply_text(
        "📚 полка с книгами\n\n"
        "мы делимся книгами, которые вдохновляют и поддерживают путь к себе ✨\n\n"
        "[Перейти в раздел](https://t.me/chatdorogakyoga/187)",
        parse_mode='Markdown'
    )

def astrology(update: Update, context: CallbackContext):
    update.message.reply_text(
        "🔮 астрология\n\n"
        "звёзды, ритмы, предназначение — всё, что помогает увидеть чуть глубже ✨\n\n"
        "[Перейти в раздел](https://t.me/chatdorogakyoga/225)",
        parse_mode='Markdown'
    )

def personal(update: Update, context: CallbackContext):
    update.message.reply_text(
        "💌 о личном из практики\n\n"
        "делимся историями, открытиями, и просто теплом 🙏\n\n"
        "[Перейти в раздел](https://t.me/chatdorogakyoga/191)",
        parse_mode='Markdown'
    )

def music(update: Update, context: CallbackContext):
    update.message.reply_text(
        "🎵 музыка\n\n"
        "плейлисты для йоги, медитации, пробуждения и просто красоты 🌀\n\n"
        "[Перейти в раздел](https://t.me/chatdorogakyoga/189)",
        parse_mode='Markdown'
    )

# Обработка текстов-кнопок
def unknown(update: Update, context: CallbackContext):
    text = update.message.text.lower()
    if "навигац" in text:
        navigation(update, context)
    elif "расписан" in text:
        schedule(update, context)
    elif "гайд" in text:
        guide(update, context)
    elif "контакт" in text:
        contacts(update, context)
    else:
        update.message.reply_text("🌿 Я тебя понял, но не совсем понял. Попробуй нажать одну из кнопок ниже.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, unknown))

    # Навигационные команды:
    dp.add_handler(CommandHandler("asanas", asanas))
    dp.add_handler(CommandHandler("pranayamas", pranayamas))
    dp.add_handler(CommandHandler("meditations", meditations))
    dp.add_handler(CommandHandler("books", books))
    dp.add_handler(CommandHandler("astrology", astrology))
    dp.add_handler(CommandHandler("personal", personal))
    dp.add_handler(CommandHandler("music", music))

    print("📲 Меню-бот запущен!")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
