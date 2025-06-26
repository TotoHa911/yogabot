from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = '7862512838:AAFTLbHVsylOGTawisvDZsvCs_6Vux5qX6E'

# Главное меню кнопками
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        ["📌 Навигация", "📅 Расписание"],
        ["📖 Гайд", "📬 Контакты"]
    ],
    resize_keyboard=True
)

def start(update: Update, context: CallbackContext):
    user = update.effective_user
    args = context.args

    if args and args[0] == "go":
        # пользователь пришёл из welcome-бота
        text = (
            f"добро пожаловать в наше пространство йоги и заботы, {user.first_name or 'друг'} 🧘‍♀️\n\n"
            "я помогу тебе сориентироваться 🌿\nвот что у нас есть:\n\n"
            "🧾 Навигация — все полезные темы\n"
            "📅 Расписание — где и когда практики\n"
            "📖 Гайд — PDF “залог удачного дня”\n"
            "📬 Контакты — если есть вопрос\n\n"
            "если просто хочется почитать интересное, поболтать — заходи в чат 🤍 [основной чат](https://t.me/chatdorogakyoga/175)"
        )
        update.message.reply_text(text, parse_mode='Markdown', reply_markup=keyboard)
    else:
        # обычный запуск бота
        update.message.reply_text(
            "нажми кнопку ниже, чтобы открыть меню 🌿",
            reply_markup=keyboard
   
    )
    update.message.reply_text(text, parse_mode='Markdown', reply_markup=keyboard)

def navigation(update: Update, context: CallbackContext):
    text = (
        "внутри группы 🧭\n\n"
        "🤸‍♀️ [асаны в деталях](https://t.me/chatdorogakyoga/177) — обсуждаем нюансы\n"
        "🌬 [пранаямы](https://t.me/chatdorogakyoga/185) — дыхание и концентрация\n"
        "📚 [книги](https://t.me/chatdorogakyoga/187) — вдохновение из текста\n"
        "🔮 [астрология](https://t.me/chatdorogakyoga/225) — про звёзды и предназначение\n"
        "💌 [о личном](https://t.me/chatdorogakyoga/191) — истории из практики\n"
        "🎵 [музыка](https://t.me/chatdorogakyoga/189) — делимся треками, достойными внимания\n\n"
        "выбирай самый интересный раздел 🌿"
    )
    update.message.reply_text(text, parse_mode='Markdown')

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

# Обработка сообщений от кнопок
def button_handler(update: Update, context: CallbackContext):
    text = update.message.text
    if "Навигация" in text:
        navigation(update, context)
    elif "Расписание" in text:
        schedule(update, context)
    elif "Гайд" in text:
        guide(update, context)
    elif "Контакт" in text:
        contacts(update, context)
    else:
        update.message.reply_text("🌿 Нажми кнопку в меню ниже, чтобы продолжить.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, button_handler))

    print("Бот запущен!")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
